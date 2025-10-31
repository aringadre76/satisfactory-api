from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import Optional
import logging
from src.parsers.game_descriptor_parser import GameDescriptorParser
from src.utils.calculations import SatisfactoryCalculator

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
    calculator = SatisfactoryCalculator(parser)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None
    calculator = None

@router.get("/production-rate")
async def get_production_rate(
    recipe: str = Query(..., description="Recipe name or class name"),
    building: Optional[str] = Query(None, description="Building type (defaults to first available)"),
    overclock: float = Query(100.0, description="Overclock percentage (100 = no overclock)", ge=1.0, le=250.0)
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_production_rate(recipe, building, overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating production rate: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate production rate")

@router.get("/buildings-needed")
async def get_buildings_needed(
    recipe: str = Query(..., description="Recipe name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    building: Optional[str] = Query(None, description="Building type (defaults to first available)"),
    overclock: float = Query(100.0, description="Overclock percentage", ge=1.0, le=250.0)
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_buildings_needed(recipe, target_rate, building, overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating buildings needed: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate buildings needed")

@router.get("/production-chain")
async def get_production_chain(
    item: str = Query(..., description="Item name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    include_alternates: bool = Query(True, description="Include alternate recipes in chain"),
    preferred_recipe: Optional[str] = Query(None, description="Preferred recipe name (for specific alternate)")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_production_chain(item, target_rate, include_alternates, preferred_recipe)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating production chain: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate production chain")

@router.get("/compare-recipes")
async def compare_recipes(
    item: str = Query(..., description="Item name or class name to compare recipes for")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.compare_recipes(item)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error comparing recipes: {e}")
        raise HTTPException(status_code=500, detail="Failed to compare recipes")

@router.get("/miner-output")
async def get_miner_output(
    resource: str = Query(..., description="Resource name"),
    miner_mk: int = Query(..., description="Miner mark (1, 2, or 3)", ge=1, le=3),
    purity: str = Query("normal", description="Purity level: impure, normal, or pure"),
    overclock: float = Query(100.0, description="Overclock percentage", ge=1.0, le=250.0)
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if purity.lower() not in ["impure", "normal", "pure"]:
        raise HTTPException(status_code=400, detail="Purity must be: impure, normal, or pure")
    
    try:
        result = calculator.calculate_miner_output(resource, miner_mk, purity, overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating miner output: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate miner output")

@router.get("/belt-requirements")
async def get_belt_requirements(
    throughput: float = Query(..., description="Required throughput (items per minute)", gt=0)
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_belt_requirements(throughput)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating belt requirements: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate belt requirements")

@router.get("/perfect-ratios")
async def get_perfect_ratios(
    item: str = Query(..., description="Item name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    include_alternates: bool = Query(True, description="Include alternate recipes"),
    preferred_recipe: Optional[str] = Query(None, description="Preferred recipe name"),
    allow_overclock: bool = Query(True, description="Allow overclocking to achieve perfect ratios")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_perfect_ratios(item, target_rate, include_alternates, preferred_recipe, allow_overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating perfect ratios: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate perfect ratios")

@router.get("/optimize-100-percent")
async def optimize_for_100_percent(
    item: str = Query(..., description="Item name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    include_alternates: bool = Query(True, description="Include alternate recipes"),
    preferred_recipe: Optional[str] = Query(None, description="Preferred recipe name"),
    allow_overclock: bool = Query(True, description="Allow overclocking to achieve 100% efficiency")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.optimize_for_100_percent_efficiency(item, target_rate, include_alternates, preferred_recipe, allow_overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error optimizing for 100% efficiency: {e}")
        raise HTTPException(status_code=500, detail="Failed to optimize for 100% efficiency")

@router.get("/factory-efficiency")
async def get_factory_efficiency(
    item: str = Query(..., description="Item name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    include_alternates: bool = Query(True, description="Include alternate recipes"),
    preferred_recipe: Optional[str] = Query(None, description="Preferred recipe name"),
    allow_overclock: bool = Query(True, description="Allow overclocking")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_factory_efficiency(item, target_rate, include_alternates, preferred_recipe, allow_overclock)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating factory efficiency: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate factory efficiency")

@router.get("/building-utilization")
async def get_building_utilization(
    item: str = Query(..., description="Item name or class name"),
    target_rate: float = Query(..., description="Target production rate (items per minute)", gt=0),
    include_alternates: bool = Query(True, description="Include alternate recipes"),
    preferred_recipe: Optional[str] = Query(None, description="Preferred recipe name")
):
    if calculator is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        result = calculator.calculate_building_utilization(item, target_rate, include_alternates, preferred_recipe)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating building utilization: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate building utilization")

