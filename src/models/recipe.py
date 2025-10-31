from pydantic import BaseModel, Field
from typing import List, Optional

class RecipeIngredient(BaseModel):
    item_class: str = Field(..., description="Game class name of the ingredient item", alias="itemClass")
    amount: int = Field(..., description="Amount of the ingredient required")

class RecipeProduct(BaseModel):
    item_class: str = Field(..., description="Game class name of the product item", alias="itemClass")
    amount: int = Field(..., description="Amount of the product produced")

class Recipe(BaseModel):
    class_name: str = Field(..., description="Game class name of the recipe", alias="className")
    display_name: str = Field(..., description="Display name of the recipe", alias="displayName")
    is_alternate: bool = Field(False, description="Whether this is an alternate recipe", alias="isAlternate")
    ingredients: List[RecipeIngredient] = Field(..., description="List of ingredients required")
    products: List[RecipeProduct] = Field(..., description="List of products produced")
    manufacturing_duration: float = Field(..., description="Production time in seconds", alias="manufacturingDuration")
    produced_in: List[str] = Field(..., description="List of buildings that can produce this recipe", alias="producedIn")
    variable_power_consumption_constant: Optional[float] = Field(None, description="Variable power consumption constant", alias="variablePowerConsumptionConstant")
    variable_power_consumption_factor: Optional[float] = Field(None, description="Variable power consumption factor", alias="variablePowerConsumptionFactor")
    
    class Config:
        populate_by_name = True

