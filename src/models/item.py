from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    item_type: str = Field(..., description="Type of item (raw_resource, component, product, etc.)", alias="itemType")
    stack_size: Optional[str] = Field(None, description="Stack size category", alias="stackSize")
    
    class Config:
        populate_by_name = True

