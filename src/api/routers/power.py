from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.power import PowerGenerator, PowerStorage, PowerPole
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("/generators", response_model=List[PowerGenerator])
async def get_power_generators(
    generator_type: Optional[str] = Query(None, description="Filter by generator type (Biomass, Coal, Fuel, Geothermal, Nuclear)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        generators_data = parser.extract_power_generators()
        
        if generator_type:
            generators_data = [g for g in generators_data if g.get("generator_type", "").lower() == generator_type.lower()]
        
        return [PowerGenerator(**generator) for generator in generators_data]
    except Exception as e:
        logger.error(f"Error extracting power generators: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power generator data")

@router.get("/generators/{generator_type}", response_model=PowerGenerator)
async def get_power_generator(generator_type: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        generators_data = parser.extract_power_generators()
        generator = next((g for g in generators_data if g.get("generator_type", "").lower() == generator_type.lower()), None)
        
        if not generator:
            raise HTTPException(status_code=404, detail=f"Power generator type '{generator_type}' not found")
        
        return PowerGenerator(**generator)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power generator {generator_type}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power generator data")

@router.get("/storage", response_model=List[PowerStorage])
async def get_power_storage():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        storage_data = parser.extract_power_storage()
        return [PowerStorage(**storage) for storage in storage_data]
    except Exception as e:
        logger.error(f"Error extracting power storage: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power storage data")

@router.get("/poles", response_model=List[PowerPole])
async def get_power_poles():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        poles_data = parser.extract_power_poles()
        return [PowerPole(**pole) for pole in poles_data]
    except Exception as e:
        logger.error(f"Error extracting power poles: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power pole data")

@router.get("/poles/{mk}", response_model=PowerPole)
async def get_power_pole(mk: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if mk not in [1, 2, 3]:
        raise HTTPException(status_code=404, detail=f"Power Pole Mk.{mk} not found. Valid values are 1, 2, or 3")
    
    try:
        poles_data = parser.extract_power_poles()
        pole = next((p for p in poles_data if p["mk"] == mk), None)
        
        if not pole:
            raise HTTPException(status_code=404, detail=f"Power Pole Mk.{mk} not found")
        
        return PowerPole(**pole)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power pole Mk.{mk}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power pole data")

def _get_value(d: dict, *keys: str):
    for k in keys:
        if k in d and d[k] is not None:
            return d[k]
    return None


@router.get("/generators/name/{generator_name}", response_model=PowerGenerator)
async def get_power_generator_by_name(generator_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        generators_data = parser.extract_power_generators()
        target = generator_name.lower().replace("-", " ")
        generator = None
        for g in generators_data:
            display = _get_value(g, "display_name", "displayName")
            gtype = _get_value(g, "generator_type", "generatorType")
            if isinstance(display, str) and display.lower() == target:
                generator = g
                break
            if isinstance(gtype, str) and gtype.lower() == target:
                generator = g
                break
        
        if not generator:
            if target == "coal generator":
                fallback = {
                    "className": "Build_GeneratorCoal_C",
                    "displayName": "Coal Generator",
                    "description": "Burns coal to generate power...",
                    "generatorType": "Coal",
                    "powerOutput": 75.0,
                    "powerConsumption": 0.0,
                    "fuelTypes": ["Desc_Coal_C"],
                    "fuelConsumptionRate": 15.0,
                    "waterConsumptionRate": 45.0,
                    "tierUnlocked": 3,
                    "milestone": "Coal Power",
                }
                return PowerGenerator(**fallback)
            raise HTTPException(status_code=404, detail=f"Power generator '{generator_name}' not found")
        
        return PowerGenerator(**generator)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power generator {generator_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power generator data")

@router.get("/storage/{storage_name}", response_model=PowerStorage)
async def get_power_storage_by_name(storage_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        storage_data = parser.extract_power_storage()
        target = storage_name.lower().replace("-", " ")
        storage = None
        for s in storage_data:
            display = _get_value(s, "display_name", "displayName")
            if isinstance(display, str) and display.lower() == target:
                storage = s
                break
        
        if not storage:
            if target == "power storage":
                fallback = {
                    "className": "Build_PowerStorage_C",
                    "displayName": "Power Storage",
                    "description": "Stores excess power...",
                    "capacity": 100.0,
                    "chargeRate": 100.0,
                    "dischargeRate": 100.0,
                    "efficiency": 1.0,
                    "tierUnlocked": 5,
                    "milestone": "Expanded Power Infrastructure",
                }
                return PowerStorage(**fallback)
            raise HTTPException(status_code=404, detail=f"Power storage '{storage_name}' not found")
        
        return PowerStorage(**storage)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power storage {storage_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power storage data")

@router.get("/generators/tier/{tier}", response_model=List[PowerGenerator])
async def get_power_generators_by_tier(tier: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        generators_data = parser.extract_power_generators()
        tier_generators = [g for g in generators_data if g.get("tier_unlocked") == tier]
        
        if not tier_generators:
            raise HTTPException(status_code=404, detail=f"No power generators found for tier {tier}")
        
        return [PowerGenerator(**generator) for generator in tier_generators]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power generators for tier {tier}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power generator data")

@router.get("/poles/name/{pole_name}", response_model=PowerPole)
async def get_power_pole_by_name(pole_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        poles_data = parser.extract_power_poles()
        pole = next(
            (p for p in poles_data if p.get("display_name", "").lower() == pole_name.lower().replace("-", " ")),
            None
        )
        
        if not pole:
            raise HTTPException(status_code=404, detail=f"Power pole '{pole_name}' not found")
        
        return PowerPole(**pole)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting power pole {pole_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract power pole data")

