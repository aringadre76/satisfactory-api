from fastapi import APIRouter, HTTPException
from pathlib import Path
from typing import List
import logging
from src.models.miner import Miner
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Miner])
async def get_miners():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        miners_data = parser.extract_miners()
        return [Miner(**miner) for miner in miners_data]
    except Exception as e:
        logger.error(f"Error extracting miners: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract miner data")

@router.get("/{mk}", response_model=Miner)
async def get_miner(mk: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if mk not in [1, 2, 3]:
        raise HTTPException(status_code=404, detail=f"Miner Mk.{mk} not found. Valid values are 1, 2, or 3")
    
    try:
        miners_data = parser.extract_miners()
        miner = next((m for m in miners_data if m["mk"] == mk), None)
        
        if not miner:
            raise HTTPException(status_code=404, detail=f"Miner Mk.{mk} not found")
        
        return Miner(**miner)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting miner Mk.{mk}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract miner data")

