from pydantic import BaseModel, Field
from typing import Optional

class TrainLocomotive(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Maximum power consumption in MW", alias="powerConsumption")
    power_consumption_min: float = Field(..., description="Minimum power consumption in MW", alias="powerConsumptionMin")
    power_consumption_max: float = Field(..., description="Maximum power consumption in MW", alias="powerConsumptionMax")
    max_speed: Optional[float] = Field(None, description="Maximum speed", alias="maxSpeed")
    
    class Config:
        populate_by_name = True

class TrainFreightCar(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    storage_slots: int = Field(..., description="Number of storage slots for solid items", alias="storageSlots")
    fluid_capacity_m3: float = Field(..., description="Fluid capacity in m³", alias="fluidCapacityM3")
    throughput_rate: Optional[float] = Field(None, description="Items per minute throughput", alias="throughputRate")
    
    class Config:
        populate_by_name = True

class TrainStation(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    platform_count: int = Field(..., description="Number of platforms", alias="platformCount")
    station_type: str = Field(..., description="Station type (solid, liquid, empty)", alias="stationType")
    
    class Config:
        populate_by_name = True

class TruckVehicle(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    vehicle_type: str = Field(..., description="Vehicle type (Truck, Tractor)", alias="vehicleType")
    storage_slots: int = Field(..., description="Number of storage slots", alias="storageSlots")
    fuel_consumption_rate: Optional[float] = Field(None, description="Fuel consumption rate", alias="fuelConsumptionRate")
    max_speed: Optional[float] = Field(None, description="Maximum speed", alias="maxSpeed")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    
    class Config:
        populate_by_name = True

class TruckStation(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    input_output_rate: Optional[float] = Field(None, description="Loading/unloading rate items per minute", alias="inputOutputRate")
    
    class Config:
        populate_by_name = True

class Drone(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    cargo_slots: int = Field(..., description="Number of cargo slots", alias="cargoSlots")
    battery_capacity: Optional[float] = Field(None, description="Battery capacity in MW", alias="batteryCapacity")
    max_speed: Optional[float] = Field(None, description="Maximum speed", alias="maxSpeed")
    range_limit: Optional[float] = Field(None, description="Maximum range", alias="rangeLimit")
    
    class Config:
        populate_by_name = True

class DroneStation(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    drone_capacity: int = Field(..., description="Number of drones supported", alias="droneCapacity")
    charging_rate: Optional[float] = Field(None, description="Charging rate in MW", alias="chargingRate")
    throughput_rate: Optional[float] = Field(None, description="Items per minute throughput", alias="throughputRate")
    
    class Config:
        populate_by_name = True

class Pipeline(BaseModel):
    mk: int = Field(..., description="Pipeline mark version (1 or 2)")
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    flow_rate: float = Field(..., description="Maximum flow rate in m³/min", alias="flowRate")
    
    class Config:
        populate_by_name = True

class PipelinePump(BaseModel):
    mk: int = Field(..., description="Pump mark version (1 or 2)")
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    head_lift: float = Field(..., description="Head lift in meters", alias="headLift")
    flow_rate: Optional[float] = Field(None, description="Flow rate in m³/min", alias="flowRate")
    
    class Config:
        populate_by_name = True

class FreightPlatform(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    storage_slots: int = Field(..., description="Number of storage slots", alias="storageSlots")
    input_rate: Optional[float] = Field(None, description="Input rate items per minute", alias="inputRate")
    output_rate: Optional[float] = Field(None, description="Output rate items per minute", alias="outputRate")
    
    class Config:
        populate_by_name = True

class RailwayTrack(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    mesh_length: float = Field(..., description="Mesh length in cm", alias="meshLength")
    power_transmission: Optional[float] = Field(None, description="Power transmission capacity in MW", alias="powerTransmission")
    connection_limit: Optional[int] = Field(None, description="Maximum connection limit", alias="connectionLimit")
    
    class Config:
        populate_by_name = True

class TrainSignal(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    signal_type: str = Field(..., description="Signal type (Block Signal, Path Signal, End Stop)", alias="signalType")
    power_consumption: Optional[float] = Field(None, description="Power consumption in MW", alias="powerConsumption")
    range: Optional[float] = Field(None, description="Signal range in meters")
    
    class Config:
        populate_by_name = True

