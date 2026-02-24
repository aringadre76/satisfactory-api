from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.item import Item
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

PAGINATION_LIMIT_MAX = 1000

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Item])
async def get_items(
    item_type: Optional[str] = Query(None, description="Filter by item type (raw_resource, component, equipment, building_part)"),
    search: Optional[str] = Query(None, description="Filter by substring match on display name or class name (case-insensitive)"),
    limit: Optional[int] = Query(None, ge=1, le=PAGINATION_LIMIT_MAX, description="Max number of results to return (applied after filters)"),
    offset: Optional[int] = Query(None, ge=0, description="Number of results to skip (applied after filters)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        items_data = parser.extract_all_items()
        
        if item_type:
            items_data = [i for i in items_data if (i.get("item_type") or "").lower() == (item_type or "").lower()]
        
        if search:
            q = search.lower()
            items_data = [i for i in items_data if q in (i.get("display_name") or "").lower() or q in (i.get("class_name") or "").lower()]
        
        items = [Item(**item) for item in items_data]
        
        if offset is not None:
            items = items[offset:]
        if limit is not None:
            items = items[:limit]
        
        return items
    except Exception as e:
        logger.error(f"Error extracting items: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract item data")

@router.get("/{item_name}", response_model=Item)
async def get_item(item_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        items_data = parser.extract_all_items()
        item = next((i for i in items_data if i["class_name"] == item_name or i["display_name"].lower() == item_name.lower()), None)
        
        if not item:
            raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found")
        
        return Item(**item)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting item {item_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract item data")

