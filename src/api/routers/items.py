from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.item import Item
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("", response_model=List[Item])
async def get_items(
    item_type: Optional[str] = Query(None, description="Filter by item type (raw_resource, component, equipment, building_part)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        items_data = parser.extract_all_items()
        
        if item_type:
            items_data = [i for i in items_data if i["item_type"] == item_type]
        
        return [Item(**item) for item in items_data]
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

