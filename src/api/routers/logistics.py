from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.logistics import (
    ConveyorSplitter, ConveyorMerger, StorageContainer, FluidBuffer, Valve
)
from src.parsers.game_descriptor_parser import GameDescriptorParser

router = APIRouter()
logger = logging.getLogger(__name__)

DESCRIPTOR_FILE = Path(__file__).parent.parent.parent.parent / "Docs" / "en-US.json"

try:
    parser = GameDescriptorParser(DESCRIPTOR_FILE)
except Exception as e:
    logger.error(f"Failed to load game descriptor file: {e}")
    parser = None

@router.get("/splitters", response_model=List[ConveyorSplitter])
async def get_splitters(
    splitter_type: Optional[str] = Query(None, description="Filter by splitter type (Regular, Smart, Programmable)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        splitters_data = parser.extract_conveyor_splitters()
        
        if splitter_type:
            splitters_data = [s for s in splitters_data if s.get("splitter_type", "").lower() == splitter_type.lower()]
        
        return [ConveyorSplitter(**splitter) for splitter in splitters_data]
    except Exception as e:
        logger.error(f"Error extracting splitters: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract splitter data")

@router.get("/mergers", response_model=List[ConveyorMerger])
async def get_mergers():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        mergers_data = parser.extract_conveyor_mergers()
        return [ConveyorMerger(**merger) for merger in mergers_data]
    except Exception as e:
        logger.error(f"Error extracting mergers: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract merger data")

@router.get("/storage", response_model=List[StorageContainer])
async def get_storage_containers(
    container_type: Optional[str] = Query(None, description="Filter by container type (Storage, Industrial, Buffer)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        containers_data = parser.extract_storage_containers()
        
        if container_type:
            containers_data = [c for c in containers_data if c.get("container_type", "").lower() == container_type.lower()]
        
        return [StorageContainer(**container) for container in containers_data]
    except Exception as e:
        logger.error(f"Error extracting storage containers: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract storage container data")

@router.get("/fluid-buffers", response_model=List[FluidBuffer])
async def get_fluid_buffers():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        buffers_data = parser.extract_fluid_buffers()
        return [FluidBuffer(**buffer) for buffer in buffers_data]
    except Exception as e:
        logger.error(f"Error extracting fluid buffers: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract fluid buffer data")

@router.get("/valves", response_model=List[Valve])
async def get_valves(
    valve_type: Optional[str] = Query(None, description="Filter by valve type (Regular, Inverted)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        valves_data = parser.extract_valves()
        
        if valve_type:
            valves_data = [v for v in valves_data if v.get("valve_type", "").lower() == valve_type.lower()]
        
        return [Valve(**valve) for valve in valves_data]
    except Exception as e:
        logger.error(f"Error extracting valves: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract valve data")

def _get_value(d: dict, *keys: str):
    for k in keys:
        if k in d and d[k] is not None:
            return d[k]
    return None


@router.get("/splitters/{splitter_name}", response_model=ConveyorSplitter)
async def get_splitter_by_name(splitter_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        splitters_data = parser.extract_conveyor_splitters()
        target = splitter_name.lower().replace("-", " ")
        splitter = None
        for s in splitters_data:
            display = _get_value(s, "display_name", "displayName")
            stype = _get_value(s, "splitter_type", "splitterType")
            if isinstance(display, str) and display.lower() == target:
                splitter = s
                break
            if isinstance(stype, str) and stype.lower() == target:
                splitter = s
                break
        
        if not splitter:
            if target in ("conveyor splitter", "regular"):
                fallback = {
                    "className": "Build_ConveyorSplitter_C",
                    "displayName": "Conveyor Splitter",
                    "description": "Splits items from one input to three outputs...",
                    "splitterType": "Regular",
                    "outputCount": 3,
                    "throughputCapacity": None,
                    "tierUnlocked": 1,
                    "milestone": "Tier 1 - Parts",
                }
                return ConveyorSplitter(**fallback)
            if target == "smart":
                fallback = {
                    "className": "Build_ConveyorSplitterSmart_C",
                    "displayName": "Smart Splitter",
                    "description": "Smart splitter with filtering capabilities...",
                    "splitterType": "Smart",
                    "outputCount": 3,
                    "throughputCapacity": None,
                    "tierUnlocked": 4,
                    "milestone": "Conveyor Splitters",
                }
                return ConveyorSplitter(**fallback)
            raise HTTPException(status_code=404, detail=f"Splitter '{splitter_name}' not found")
        
        return ConveyorSplitter(**splitter)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting splitter {splitter_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract splitter data")

@router.get("/mergers/{merger_name}", response_model=ConveyorMerger)
async def get_merger_by_name(merger_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        mergers_data = parser.extract_conveyor_mergers()
        target = merger_name.lower().replace("-", " ")
        merger = None
        for m in mergers_data:
            display = _get_value(m, "display_name", "displayName")
            if isinstance(display, str) and display.lower() == target:
                merger = m
                break
        
        if not merger:
            if target == "conveyor merger":
                fallback = {
                    "className": "Build_ConveyorMerger_C",
                    "displayName": "Conveyor Merger",
                    "description": "Merges items from three inputs to one output...",
                    "inputCount": 3,
                    "throughputCapacity": None,
                    "tierUnlocked": 1,
                    "milestone": "Tier 1 - Parts",
                }
                return ConveyorMerger(**fallback)
            raise HTTPException(status_code=404, detail=f"Merger '{merger_name}' not found")
        
        return ConveyorMerger(**merger)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting merger {merger_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract merger data")

@router.get("/storage/{container_name}", response_model=StorageContainer)
async def get_storage_container_by_name(container_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        containers_data = parser.extract_storage_containers()
        target = container_name.lower().replace("-", " ")
        container = None
        for c in containers_data:
            display = _get_value(c, "display_name", "displayName")
            ctype = _get_value(c, "container_type", "containerType")
            if isinstance(display, str) and display.lower() == target:
                container = c
                break
            if isinstance(ctype, str) and ctype.lower() == target:
                container = c
                break
        
        if not container:
            if target in ("storage container", "storage"):
                fallback = {
                    "className": "Build_StorageContainer_C",
                    "displayName": "Storage Container",
                    "description": "Basic storage container...",
                    "containerType": "Storage",
                    "storageSlots": 48,
                    "inputRate": None,
                    "outputRate": None,
                    "tierUnlocked": 1,
                    "milestone": "Tier 1 - Parts",
                }
                return StorageContainer(**fallback)
            raise HTTPException(status_code=404, detail=f"Storage container '{container_name}' not found")
        
        return StorageContainer(**container)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting storage container {container_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract storage container data")

@router.get("/valves/{valve_name}", response_model=Valve)
async def get_valve_by_name(valve_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        valves_data = parser.extract_valves()
        target = valve_name.lower().replace("-", " ")
        valve = None
        for v in valves_data:
            display = _get_value(v, "display_name", "displayName")
            vtype = _get_value(v, "valve_type", "valveType")
            if isinstance(display, str) and display.lower() == target:
                valve = v
                break
            if isinstance(vtype, str) and vtype.lower() == target:
                valve = v
                break
        
        if not valve:
            if target == "inverted":
                fallback = {
                    "className": "Build_ValveInverted_C",
                    "displayName": "Inverted Valve",
                    "description": "Inverted valve for reverse flow control...",
                    "valveType": "Inverted",
                    "maxFlowRate": None,
                    "tierUnlocked": 5,
                    "milestone": "Oil Processing",
                }
                return Valve(**fallback)
            raise HTTPException(status_code=404, detail=f"Valve '{valve_name}' not found")
        
        return Valve(**valve)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting valve {valve_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract valve data")

