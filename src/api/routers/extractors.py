from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.extractors import WaterExtractor, ResourceWellExtractor
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("/water-extractors", response_model=List[WaterExtractor])
async def get_water_extractors():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        extractors_data = parser.extract_water_extractors()
        return [WaterExtractor(**extractor) for extractor in extractors_data]
    except Exception as e:
        logger.error(f"Error extracting water extractors: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract water extractor data")

@router.get("/resource-well-extractors", response_model=List[ResourceWellExtractor])
async def get_resource_well_extractors(
    resource_type: Optional[str] = Query(None, description="Filter by resource type (Oil, Nitrogen, etc.)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        extractors_data = parser.extract_resource_well_extractors()
        
        if resource_type:
            extractors_data = [e for e in extractors_data if e.get("resource_type", "").lower() == resource_type.lower()]
        
        return [ResourceWellExtractor(**extractor) for extractor in extractors_data]
    except Exception as e:
        logger.error(f"Error extracting resource well extractors: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract resource well extractor data")

@router.get("/water-extractors/{extractor_name}", response_model=WaterExtractor)
async def get_water_extractor_by_name(extractor_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        extractors_data = parser.extract_water_extractors()
        extractor = next(
            (e for e in extractors_data if e.get("display_name", "").lower() == extractor_name.lower().replace("-", " ")),
            None
        )
        
        if not extractor:
            raise HTTPException(status_code=404, detail=f"Water extractor '{extractor_name}' not found")
        
        return WaterExtractor(**extractor)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting water extractor {extractor_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract water extractor data")

