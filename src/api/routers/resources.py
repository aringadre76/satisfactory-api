from fastapi import APIRouter, HTTPException
from pathlib import Path
from typing import List
import logging
from src.models.resource_node import ResourceNode
from src.models.raw_resource import RawResource
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("/resource-nodes", response_model=List[ResourceNode])
async def get_resource_nodes():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        nodes_data = parser.extract_resource_nodes()
        return [ResourceNode(**node) for node in nodes_data]
    except Exception as e:
        logger.error(f"Error extracting resource nodes: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract resource node data")

@router.get("/raw-resources", response_model=List[RawResource])
async def get_raw_resources():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        resources_data = parser.extract_raw_resources()
        return [RawResource(**resource) for resource in resources_data]
    except Exception as e:
        logger.error(f"Error extracting raw resources: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract raw resource data")

@router.get("/wiki/{item}")
async def get_wiki_reference(item: str):
    from src.utils.wiki_helper import get_wiki_url
    wiki_url = get_wiki_url(item)
    return {
        "item": item,
        "wiki_url": wiki_url
    }

