from pydantic import BaseModel, Field
from typing import Optional

class Building(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    building_type: str = Field(..., description="Type of building (Constructor, Assembler, Manufacturer, etc.)", alias="buildingType")
    power_consumption: float = Field(..., description="Base power consumption in MW", alias="powerConsumption")
    power_consumption_exponent: Optional[float] = Field(None, description="Power consumption exponent for overclocking", alias="powerConsumptionExponent")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

