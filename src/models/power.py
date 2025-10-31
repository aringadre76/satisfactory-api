from pydantic import BaseModel, Field
from typing import Optional

class PowerGenerator(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    generator_type: str = Field(..., description="Generator type (Biomass, Coal, Fuel, Geothermal, Nuclear)", alias="generatorType")
    power_output: float = Field(..., description="Power output in MW", alias="powerOutput")
    power_consumption: Optional[float] = Field(None, description="Power consumption in MW", alias="powerConsumption")
    fuel_types: Optional[list] = Field(None, description="List of accepted fuel types", alias="fuelTypes")
    fuel_consumption_rate: Optional[float] = Field(None, description="Fuel consumption rate", alias="fuelConsumptionRate")
    water_consumption_rate: Optional[float] = Field(None, description="Water consumption rate in m³/min", alias="waterConsumptionRate")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class PowerStorage(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    capacity: float = Field(..., description="Storage capacity in MWh", alias="capacity")
    charge_rate: Optional[float] = Field(None, description="Charge rate in MW", alias="chargeRate")
    discharge_rate: Optional[float] = Field(None, description="Discharge rate in MW", alias="dischargeRate")
    efficiency: Optional[float] = Field(None, description="Efficiency percentage", alias="efficiency")
    tier_unlocked: Optional[int] = Field(None, description="Tier when unlocked", alias="tierUnlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    
    class Config:
        populate_by_name = True

class PowerPole(BaseModel):
    mk: int = Field(..., description="Power pole mark version (1, 2, or 3)")
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    connection_limit: int = Field(..., description="Maximum connection limit", alias="connectionLimit")
    power_transmission: Optional[float] = Field(None, description="Power transmission capacity in MW", alias="powerTransmission")
    
    class Config:
        populate_by_name = True

