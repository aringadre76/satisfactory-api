from pydantic import BaseModel, Field
from typing import Optional

class WaterExtractor(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    extraction_rate: float = Field(..., description="Base extraction rate in m³/min", alias="extractionRate")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    power_consumption_exponent: Optional[float] = Field(None, description="Power consumption exponent for overclocking", alias="powerConsumptionExponent")
    
    class Config:
        populate_by_name = True

class ResourceWellExtractor(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    resource_type: str = Field(..., description="Resource type (Oil, Nitrogen, etc.)", alias="resourceType")
    extraction_rate: Optional[float] = Field(None, description="Extraction rate", alias="extractionRate")
    power_consumption: float = Field(..., description="Power consumption in MW", alias="powerConsumption")
    pressure_requirement: Optional[float] = Field(None, description="Pressure requirement", alias="pressureRequirement")
    
    class Config:
        populate_by_name = True

