from pydantic import BaseModel, Field
from typing import Optional

class RawResource(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    resource_type: str = Field(..., description="Type of resource", alias="resourceType")
    
    class Config:
        populate_by_name = True

