from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.progression import Milestone, Unlock
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("/milestones", response_model=List[Milestone])
async def get_milestones(
    tier: Optional[int] = Query(None, description="Filter by tier number"),
    phase: Optional[int] = Query(None, description="Filter by phase number")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        milestones_data = parser.extract_milestones()
        
        if tier is not None:
            milestones_data = [m for m in milestones_data if m.get("tier") == tier]
        
        if phase is not None:
            milestones_data = [m for m in milestones_data if m.get("phase") == phase]
        
        return [Milestone(**milestone) for milestone in milestones_data]
    except Exception as e:
        logger.error(f"Error extracting milestones: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract milestone data")

@router.get("/milestones/{tier}", response_model=List[Milestone])
async def get_milestones_by_tier(tier: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        milestones_data = parser.extract_milestones()
        tier_milestones = [m for m in milestones_data if m.get("tier") == tier]
        
        if not tier_milestones:
            raise HTTPException(status_code=404, detail=f"No milestones found for tier {tier}")
        
        return [Milestone(**milestone) for milestone in tier_milestones]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting milestones for tier {tier}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract milestone data")

@router.get("/milestones/name/{milestone_name}", response_model=Milestone)
async def get_milestone_by_name(milestone_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        milestones_data = parser.extract_milestones()
        milestone = next(
            (m for m in milestones_data if m.get("display_name", "").lower() == milestone_name.lower()),
            None
        )
        
        if not milestone:
            raise HTTPException(status_code=404, detail=f"Milestone '{milestone_name}' not found")
        
        return Milestone(**milestone)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting milestone {milestone_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract milestone data")

@router.get("/unlocks", response_model=List[Unlock])
async def get_unlocks(
    unlock_type: Optional[str] = Query(None, description="Filter by unlock type (building, recipe, schematic)"),
    tier: Optional[int] = Query(None, description="Filter by tier number"),
    milestone: Optional[str] = Query(None, description="Filter by milestone name")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        unlocks_data = parser.extract_unlocks()
        
        if unlock_type:
            unlocks_data = [u for u in unlocks_data if u.get("unlock_type", "").lower() == unlock_type.lower()]
        
        if tier is not None:
            unlocks_data = [u for u in unlocks_data if u.get("tier") == tier]
        
        if milestone:
            unlocks_data = [u for u in unlocks_data if u.get("milestone", "").lower() == milestone.lower()]
        
        return [Unlock(**unlock) for unlock in unlocks_data]
    except Exception as e:
        logger.error(f"Error extracting unlocks: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract unlock data")

@router.get("/unlocks/{unlock_name}", response_model=Unlock)
async def get_unlock_by_name(unlock_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        unlocks_data = parser.extract_unlocks()
        unlock = next(
            (u for u in unlocks_data if u.get("display_name", "").lower() == unlock_name.lower().replace("-", " ") or 
             u.get("class_name", "").lower() == unlock_name.lower()),
            None
        )
        
        if not unlock:
            raise HTTPException(status_code=404, detail=f"Unlock '{unlock_name}' not found")
        
        return Unlock(**unlock)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting unlock {unlock_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract unlock data")

@router.get("/unlocks/type/{unlock_type}", response_model=List[Unlock])
async def get_unlocks_by_type(unlock_type: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    unlock_type_lower = unlock_type.lower()
    valid_types = ["building", "recipe", "schematic"]
    
    if unlock_type_lower not in valid_types:
        raise HTTPException(status_code=404, detail=f"Unlock type '{unlock_type}' not found. Valid values are: building, recipe, schematic")
    
    try:
        unlocks_data = parser.extract_unlocks()
        type_unlocks = [u for u in unlocks_data if u.get("unlock_type", "").lower() == unlock_type_lower]
        return [Unlock(**unlock) for unlock in type_unlocks]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting unlocks for type {unlock_type}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract unlock data")
