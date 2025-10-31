from pydantic import BaseModel, Field
from typing import Optional

class Miner(BaseModel):
    mk: int = Field(..., description="Miner mark version (1, 2, or 3)")
    class_name: str = Field(..., description="Game class name")
    display_name: str = Field(..., description="Display name")
    description: str = Field(..., description="Description")
    extract_cycle_time: float = Field(..., description="Extraction cycle time in seconds", alias="extractCycleTime")
    items_per_cycle: int = Field(..., description="Items extracted per cycle", alias="itemsPerCycle")
    power_consumption: float = Field(..., description="Base power consumption in MW", alias="powerConsumption")
    power_consumption_exponent: Optional[float] = Field(None, description="Power consumption exponent for overclocking", alias="powerConsumptionExponent")
    extract_startup_time: Optional[float] = Field(None, description="Extraction startup time in seconds", alias="extractStartupTime")
    
    class Config:
        populate_by_name = True

