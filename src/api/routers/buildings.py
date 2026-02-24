from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.building import Building
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Building])
async def get_buildings(
    building_type: Optional[str] = Query(None, description="Filter by building type (e.g., Constructor, Assembler)"),
    unlocked_by_tier: Optional[int] = Query(None, description="Filter to buildings unlocked at this tier (uses progression data)"),
    unlocked_by_milestone: Optional[str] = Query(None, description="Filter to buildings unlocked by this milestone (display name, case-insensitive)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        buildings_data = parser.extract_buildings()
        
        if unlocked_by_tier is not None or unlocked_by_milestone is not None:
            unlocked = parser.get_unlocked_class_names(tier=unlocked_by_tier, milestone=unlocked_by_milestone)
            allowed = unlocked["building"]
            buildings_data = [b for b in buildings_data if b.get("class_name") in allowed]
        
        if building_type:
            buildings_data = [b for b in buildings_data if b["building_type"].lower() == building_type.lower()]
        
        return [Building(**building) for building in buildings_data]
    except Exception as e:
        logger.error(f"Error extracting buildings: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract building data")

@router.get("/{building_type}", response_model=Building)
async def get_building(building_type: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        buildings_data = parser.extract_buildings()
        building = next((b for b in buildings_data if b["building_type"].lower() == building_type.lower()), None)
        
        if not building:
            raise HTTPException(status_code=404, detail=f"Building type '{building_type}' not found")
        
        return Building(**building)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting building {building_type}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract building data")

