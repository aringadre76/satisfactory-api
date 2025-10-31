from pydantic import BaseModel, Field
from typing import Optional

class ConveyorSplitter(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    splitter_type: str = Field(..., description="Splitter type (Regular, Smart, Programmable)", alias="splitterType")
    output_count: int = Field(..., description="Number of output connections", alias="outputCount")
    throughput_capacity: Optional[float] = Field(None, description="Throughput capacity items per minute", alias="throughputCapacity")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class ConveyorMerger(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    input_count: int = Field(..., description="Number of input connections", alias="inputCount")
    throughput_capacity: Optional[float] = Field(None, description="Throughput capacity items per minute", alias="throughputCapacity")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class StorageContainer(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    container_type: str = Field(..., description="Container type (Storage, Industrial, Buffer)", alias="containerType")
    storage_slots: int = Field(..., description="Number of storage slots", alias="storageSlots")
    input_rate: Optional[float] = Field(None, description="Input rate items per minute", alias="inputRate")
    output_rate: Optional[float] = Field(None, description="Output rate items per minute", alias="outputRate")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class FluidBuffer(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    capacity: float = Field(..., description="Storage capacity in m³", alias="capacity")
    input_rate: Optional[float] = Field(None, description="Input flow rate in m³/min", alias="inputRate")
    output_rate: Optional[float] = Field(None, description="Output flow rate in m³/min", alias="outputRate")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class Valve(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    valve_type: str = Field(..., description="Valve type (Regular, Inverted)", alias="valveType")
    max_flow_rate: Optional[float] = Field(None, description="Maximum flow rate in m³/min", alias="maxFlowRate")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

