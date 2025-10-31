from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from typing import List, Optional
import logging
from src.models.transportation import (
    Pipeline, PipelinePump, TrainStation, TruckStation, 
    DroneStation, TrainLocomotive, TrainFreightCar, TruckVehicle, Drone, FreightPlatform,
    RailwayTrack, TrainSignal
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

@router.get("/pipelines", response_model=List[Pipeline])
async def get_pipelines():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        pipelines_data = parser.extract_pipelines()
        return [Pipeline(**pipeline) for pipeline in pipelines_data]
    except Exception as e:
        logger.error(f"Error extracting pipelines: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract pipeline data")

@router.get("/pipelines/{mk}", response_model=Pipeline)
async def get_pipeline(mk: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if mk not in [1, 2]:
        raise HTTPException(status_code=404, detail=f"Pipeline Mk.{mk} not found. Valid values are 1 or 2")
    
    try:
        pipelines_data = parser.extract_pipelines()
        pipeline = next((p for p in pipelines_data if p["mk"] == mk), None)
        
        if not pipeline:
            raise HTTPException(status_code=404, detail=f"Pipeline Mk.{mk} not found")
        
        return Pipeline(**pipeline)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting pipeline Mk.{mk}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract pipeline data")

@router.get("/pipeline-pumps", response_model=List[PipelinePump])
async def get_pipeline_pumps():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        pumps_data = parser.extract_pipeline_pumps()
        return [PipelinePump(**pump) for pump in pumps_data]
    except Exception as e:
        logger.error(f"Error extracting pipeline pumps: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract pipeline pump data")

@router.get("/pipeline-pumps/{mk}", response_model=PipelinePump)
async def get_pipeline_pump(mk: int):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    if mk not in [1, 2]:
        raise HTTPException(status_code=404, detail=f"Pipeline Pump Mk.{mk} not found. Valid values are 1 or 2")
    
    try:
        pumps_data = parser.extract_pipeline_pumps()
        pump = next((p for p in pumps_data if p["mk"] == mk), None)
        
        if not pump:
            raise HTTPException(status_code=404, detail=f"Pipeline Pump Mk.{mk} not found")
        
        return PipelinePump(**pump)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting pipeline pump Mk.{mk}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract pipeline pump data")

@router.get("/train-stations", response_model=List[TrainStation])
async def get_train_stations(
    station_type: Optional[str] = Query(None, description="Filter by station type (solid, liquid, empty)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        stations_data = parser.extract_train_stations()
        
        if station_type:
            stations_data = [s for s in stations_data if s.get("station_type", "").lower() == station_type.lower()]
        
        return [TrainStation(**station) for station in stations_data]
    except Exception as e:
        logger.error(f"Error extracting train stations: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract train station data")

@router.get("/truck-stations", response_model=List[TruckStation])
async def get_truck_stations():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        stations_data = parser.extract_truck_stations()
        return [TruckStation(**station) for station in stations_data]
    except Exception as e:
        logger.error(f"Error extracting truck stations: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract truck station data")

@router.get("/drone-stations", response_model=List[DroneStation])
async def get_drone_stations():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        stations_data = parser.extract_drone_stations()
        return [DroneStation(**station) for station in stations_data]
    except Exception as e:
        logger.error(f"Error extracting drone stations: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract drone station data")

@router.get("/trains/locomotives", response_model=List[TrainLocomotive])
async def get_train_locomotives():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        locomotives_data = parser.extract_train_locomotives()
        return [TrainLocomotive(**locomotive) for locomotive in locomotives_data]
    except Exception as e:
        logger.error(f"Error extracting train locomotives: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract locomotive data")

@router.get("/trains/freight-cars", response_model=List[TrainFreightCar])
async def get_train_freight_cars():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        freight_cars_data = parser.extract_train_freight_cars()
        return [TrainFreightCar(**car) for car in freight_cars_data]
    except Exception as e:
        logger.error(f"Error extracting freight cars: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract freight car data")

@router.get("/vehicles/trucks", response_model=List[TruckVehicle])
async def get_trucks():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        trucks_data = parser.extract_trucks()
        return [TruckVehicle(**truck) for truck in trucks_data]
    except Exception as e:
        logger.error(f"Error extracting trucks: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract truck data")

@router.get("/vehicles/trucks/{vehicle_type}", response_model=TruckVehicle)
async def get_truck(vehicle_type: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    vehicle_type_lower = vehicle_type.lower()
    if vehicle_type_lower not in ["truck", "tractor"]:
        raise HTTPException(status_code=404, detail=f"Vehicle type '{vehicle_type}' not found. Valid values are: truck, tractor")
    
    try:
        trucks_data = parser.extract_trucks()
        truck = next((t for t in trucks_data if t.get("vehicle_type", "").lower() == vehicle_type_lower), None)
        
        if not truck:
            raise HTTPException(status_code=404, detail=f"Vehicle type '{vehicle_type}' not found")
        
        return TruckVehicle(**truck)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting truck {vehicle_type}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract truck data")

@router.get("/drones", response_model=List[Drone])
async def get_drones():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        drones_data = parser.extract_drones()
        return [Drone(**drone) for drone in drones_data]
    except Exception as e:
        logger.error(f"Error extracting drones: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract drone data")

@router.get("/freight-platforms", response_model=List[FreightPlatform])
async def get_freight_platforms():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        platforms_data = parser.extract_freight_platforms()
        return [FreightPlatform(**platform) for platform in platforms_data]
    except Exception as e:
        logger.error(f"Error extracting freight platforms: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract freight platform data")

@router.get("/railway-tracks", response_model=List[RailwayTrack])
async def get_railway_tracks():
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        tracks_data = parser.extract_railway_tracks()
        return [RailwayTrack(**track) for track in tracks_data]
    except Exception as e:
        logger.error(f"Error extracting railway tracks: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract railway track data")

@router.get("/trains/signals", response_model=List[TrainSignal])
async def get_train_signals(
    signal_type: Optional[str] = Query(None, description="Filter by signal type (Block Signal, Path Signal, End Stop)")
):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        signals_data = parser.extract_train_signals()
        
        if signal_type:
            signals_data = [s for s in signals_data if s.get("signal_type", "").lower() == signal_type.lower()]
        
        return [TrainSignal(**signal) for signal in signals_data]
    except Exception as e:
        logger.error(f"Error extracting train signals: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract train signal data")

@router.get("/trains/signals/{signal_type}", response_model=TrainSignal)
async def get_train_signal(signal_type: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    signal_type_lower = signal_type.lower().replace("-", " ").replace("_", " ")
    valid_types = ["block signal", "path signal", "end stop"]
    
    if signal_type_lower not in valid_types:
        raise HTTPException(status_code=404, detail=f"Signal type '{signal_type}' not found. Valid values are: Block Signal, Path Signal, End Stop")
    
    try:
        signals_data = parser.extract_train_signals()
        signal = next((s for s in signals_data if s.get("signal_type", "").lower() == signal_type_lower), None)
        
        if not signal:
            raise HTTPException(status_code=404, detail=f"Signal type '{signal_type}' not found")
        
        return TrainSignal(**signal)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting train signal {signal_type}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract train signal data")

@router.get("/trains/locomotives/{locomotive_name}", response_model=TrainLocomotive)
async def get_train_locomotive_by_name(locomotive_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        locomotives_data = parser.extract_train_locomotives()
        locomotive = next(
            (l for l in locomotives_data if l.get("display_name", "").lower() == locomotive_name.lower()),
            None
        )
        
        if not locomotive:
            raise HTTPException(status_code=404, detail=f"Locomotive '{locomotive_name}' not found")
        
        return TrainLocomotive(**locomotive)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting locomotive {locomotive_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract locomotive data")

@router.get("/trains/freight-cars/{car_name}", response_model=TrainFreightCar)
async def get_train_freight_car_by_name(car_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        freight_cars_data = parser.extract_train_freight_cars()
        freight_car = next(
            (c for c in freight_cars_data if c.get("display_name", "").lower() == car_name.lower()),
            None
        )
        
        if not freight_car:
            raise HTTPException(status_code=404, detail=f"Freight car '{car_name}' not found")
        
        return TrainFreightCar(**freight_car)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting freight car {car_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract freight car data")

@router.get("/drones/{drone_name}", response_model=Drone)
async def get_drone_by_name(drone_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        drones_data = parser.extract_drones()
        drone = next(
            (d for d in drones_data if d.get("display_name", "").lower() == drone_name.lower()),
            None
        )
        
        if not drone:
            raise HTTPException(status_code=404, detail=f"Drone '{drone_name}' not found")
        
        return Drone(**drone)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting drone {drone_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract drone data")

@router.get("/train-stations/{station_name}", response_model=TrainStation)
async def get_train_station_by_name(station_name: str):
    if parser is None:
        raise HTTPException(status_code=500, detail="Game descriptor data not available")
    
    try:
        stations_data = parser.extract_train_stations()
        station = next(
            (s for s in stations_data if s.get("display_name", "").lower() == station_name.lower().replace("-", " ")),
            None
        )
        
        if not station:
            raise HTTPException(status_code=404, detail=f"Train station '{station_name}' not found")
        
        return TrainStation(**station)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error extracting train station {station_name}: {e}")
        raise HTTPException(status_code=500, detail="Failed to extract train station data")

