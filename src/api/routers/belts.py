from fastapi import APIRouter, HTTPException
from pathlib import Path
from typing import List
import logging
from src.models.belt import Belt
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Belt])
async def get_belts():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        belts_data = parser.extract_belts()
        return [Belt(**belt) for belt in belts_data]
    except Exception as e:
        logger.error(f"Error extracting belts: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract belt data")

@router.get("/{mk}", response_model=Belt)
async def get_belt(mk: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if mk not in [1, 2, 3, 4, 5, 6]:
        raise HTTPException(status_code=404, detail=f"Belt Mk.{mk} not found. Valid values are 1 through 6")
    
    try:
        belts_data = parser.extract_belts()
        belt = next((b for b in belts_data if b["mk"] == mk), None)
        
        if not belt:
            raise HTTPException(status_code=404, detail=f"Belt Mk.{mk} not found")
        
        return Belt(**belt)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting belt Mk.{mk}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract belt data")

