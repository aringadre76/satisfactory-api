from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.recipe import Recipe, RecipeIngredient, RecipeProduct
from src.parsers.game_descriptor_parser import GameDescriptorParser
from src.utils.calculations import find_recipes_by_product

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

PAGINATION_LIMIT_MAX = 1000

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Recipe])
async def get_recipes(
    alternate_only: Optional[bool] = Query(None, description="Filter to only alternate recipes"),
    building: Optional[str] = Query(None, description="Filter by building type (e.g., Constructor, Assembler). Case-insensitive."),
    search: Optional[str] = Query(None, description="Filter by substring match on display name or class name (case-insensitive)"),
    produces: Optional[str] = Query(None, description="Filter to recipes that output this item (by display name or class name, case-insensitive)"),
    unlocked_by_tier: Optional[int] = Query(None, description="Filter to recipes unlocked at this tier (uses progression data)"),
    unlocked_by_milestone: Optional[str] = Query(None, description="Filter to recipes unlocked by this milestone (display name, case-insensitive)"),
    limit: Optional[int] = Query(None, ge=1, le=PAGINATION_LIMIT_MAX, description="Max number of results to return (applied after filters)"),
    offset: Optional[int] = Query(None, ge=0, description="Number of results to skip (applied after filters)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        recipes_data = parser.extract_recipes()
        
        if produces is not None:
            recipes_data = find_recipes_by_product(parser, produces)
        
        if unlocked_by_tier is not None or unlocked_by_milestone is not None:
            unlocked = parser.get_unlocked_class_names(tier=unlocked_by_tier, milestone=unlocked_by_milestone)
            allowed = unlocked["recipe"]
            recipes_data = [r for r in recipes_data if r.get("class_name") in allowed]
        
        if alternate_only is not None:
            recipes_data = [r for r in recipes_data if r["is_alternate"] == alternate_only]
        
        if building:
            building_lower = building.lower()
            recipes_data = [r for r in recipes_data if any(entry.lower() == building_lower for entry in r.get("produced_in", []))]
        
        if search:
            q = search.lower()
            recipes_data = [r for r in recipes_data if q in (r.get("display_name") or "").lower() or q in (r.get("class_name") or "").lower()]
        
        recipes = []
        for recipe_data in recipes_data:
            ingredients = [
                RecipeIngredient(
                    itemClass=ing["item_class"],
                    amount=ing["amount"]
                ) for ing in recipe_data["ingredients"]
            ]
            products = [
                RecipeProduct(
                    itemClass=prod["item_class"],
                    amount=prod["amount"]
                ) for prod in recipe_data["products"]
            ]
            recipe_obj = Recipe(
                className=recipe_data["class_name"],
                displayName=recipe_data["display_name"],
                isAlternate=recipe_data["is_alternate"],
                ingredients=ingredients,
                products=products,
                manufacturingDuration=recipe_data["manufacturing_duration"],
                producedIn=recipe_data["produced_in"],
                variablePowerConsumptionConstant=recipe_data.get("variable_power_consumption_constant"),
                variablePowerConsumptionFactor=recipe_data.get("variable_power_consumption_factor")
            )
            recipes.append(recipe_obj)
        
        if offset is not None:
            recipes = recipes[offset:]
        if limit is not None:
            recipes = recipes[:limit]
        
        return recipes
    except Exception as e:
        logger.error(f"Error extracting recipes: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract recipe data")

@router.get("/{recipe_name}", response_model=Recipe)
async def get_recipe(recipe_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        recipes_data = parser.extract_recipes()
        recipe = next((r for r in recipes_data if r["class_name"] == recipe_name or (r.get("display_name") or "").lower() == recipe_name.lower()), None)
        
        if not recipe:
            raise HTTPException(status_code=404, detail=f"Recipe '{recipe_name}' not found")
        
        ingredients = [
            RecipeIngredient(
                itemClass=ing["item_class"],
                amount=ing["amount"]
            ) for ing in recipe["ingredients"]
        ]
        products = [
            RecipeProduct(
                itemClass=prod["item_class"],
                amount=prod["amount"]
            ) for prod in recipe["products"]
        ]
        
        return Recipe(
            className=recipe["class_name"],
            displayName=recipe["display_name"],
            isAlternate=recipe["is_alternate"],
            ingredients=ingredients,
            products=products,
            manufacturingDuration=recipe["manufacturing_duration"],
            producedIn=recipe["produced_in"],
            variablePowerConsumptionConstant=recipe.get("variable_power_consumption_constant"),
            variablePowerConsumptionFactor=recipe.get("variable_power_consumption_factor")
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting recipe {recipe_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract recipe data")

