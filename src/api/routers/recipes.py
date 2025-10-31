from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.recipe import Recipe, RecipeIngredient, RecipeProduct
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Recipe])
async def get_recipes(
    alternate_only: Optional[bool] = Query(None, description="Filter to only alternate recipes"),
    building: Optional[str] = Query(None, description="Filter by building type (e.g., Constructor, Assembler)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        recipes_data = parser.extract_recipes()
        
        if alternate_only is not None:
            recipes_data = [r for r in recipes_data if r["is_alternate"] == alternate_only]
        
        if building:
            recipes_data = [r for r in recipes_data if building in r.get("produced_in", [])]
        
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
        recipe = next((r for r in recipes_data if r["class_name"] == recipe_name or r["display_name"].lower() == recipe_name.lower()), None)
        
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

