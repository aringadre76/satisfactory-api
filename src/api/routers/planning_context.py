from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging
from src.models.item import Item
from src.models.recipe import Recipe, RecipeIngredient, RecipeProduct
from src.models.building import Building
from src.models.belt import Belt
from src.models.miner import Miner
from src.models.resource_node import ResourceNode
from src.models.raw_resource import RawResource
from src.models.progression import Milestone, Unlock
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

OVERCLOCK_PRESETS = {"min": 1, "max": 250, "presets": [100, 125, 150, 200, 250]}

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None


def _effective_tier(tier: Optional[int], milestone: Optional[str]) -> Optional[int]:
    if tier is not None:
        return tier
    if not milestone or parser is None:
        return None
    milestones_data = parser.extract_milestones()
    for m in milestones_data:
        if (m.get("display_name") or "").lower() == milestone.lower():
            t = m.get("tier")
            return int(t) if t is not None else None
    return None


def _filter_buildings_by_progression(buildings_data: List[Dict[str, Any]], tier: Optional[int], milestone: Optional[str]) -> List[Dict[str, Any]]:
    if tier is None and not milestone:
        return buildings_data
    effective = _effective_tier(tier, milestone)
    if effective is None:
        return buildings_data
    out = []
    for b in buildings_data:
        t = b.get("tier_unlocked")
        if t is None or t <= effective:
            out.append(b)
    return out


@router.get("", response_model=Dict[str, Any])
async def get_planning_context(
    tier: Optional[int] = Query(None, description="Filter items, recipes, and buildings to those unlocked at or before this tier"),
    milestone: Optional[str] = Query(None, description="Filter by milestone name (resolves to tier; same semantics as tier when provided)"),
    include_progression: bool = Query(False, description="Include milestones and unlocks in the response")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")

    try:
        items_data = parser.extract_all_items()
        recipes_data = parser.extract_recipes()
        buildings_data = parser.extract_buildings()
        buildings_data = _filter_buildings_by_progression(buildings_data, tier, milestone)

        if tier is not None or milestone:
            unlocked = parser.get_unlocked_class_names(tier=tier, milestone=milestone)
            recipes_data = [r for r in recipes_data if r.get("class_name") in unlocked.get("recipe", set())]
            items_data = [i for i in items_data if i.get("class_name") in unlocked.get("schematic", set())]

        belts_data = parser.extract_belts()
        miners_data = parser.extract_miners()
        nodes_data = parser.extract_resource_nodes()
        raw_resources_data = parser.extract_raw_resources()

        items = [Item(**i) for i in items_data]
        recipes = []
        for r in recipes_data:
            recipes.append(Recipe(
                className=r["class_name"],
                displayName=r["display_name"],
                isAlternate=r["is_alternate"],
                ingredients=[RecipeIngredient(itemClass=ing["item_class"], amount=ing["amount"]) for ing in r["ingredients"]],
                products=[RecipeProduct(itemClass=p["item_class"], amount=p["amount"]) for p in r["products"]],
                manufacturingDuration=r["manufacturing_duration"],
                producedIn=r["produced_in"],
                variablePowerConsumptionConstant=r.get("variable_power_consumption_constant"),
                variablePowerConsumptionFactor=r.get("variable_power_consumption_factor"),
            ))
        buildings = [Building(**b) for b in buildings_data]
        belts = [Belt(**b) for b in belts_data]
        miners = [Miner(**m) for m in miners_data]
        resource_nodes = [ResourceNode(**n) for n in nodes_data]
        raw_resources = [RawResource(**r) for r in raw_resources_data]

        payload: Dict[str, Any] = {
            "items": items,
            "recipes": recipes,
            "buildings": buildings,
            "belts": belts,
            "miners": miners,
            "resource_nodes": resource_nodes,
            "raw_resources": raw_resources,
            "overclock": OVERCLOCK_PRESETS,
        }

        if include_progression:
            milestones_data = parser.extract_milestones()
            unlocks_data = parser.extract_unlocks()
            effective = _effective_tier(tier, milestone)
            if effective is not None:
                milestones_data = [m for m in milestones_data if m.get("tier") is not None and m.get("tier") <= effective]
                unlocks_data = [u for u in unlocks_data if u.get("tier") is None or u.get("tier") <= effective]
            payload["progression"] = {
                "milestones": [Milestone(**m) for m in milestones_data],
                "unlocks": [Unlock(**u) for u in unlocks_data],
            }

        return payload
    except Exception as e:
        logger.error(f"Error building planning context: {e}")
        raise HTTPException(status_code=500, detail="Failed to build planning context")
