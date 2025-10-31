from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class PurityLevel(str, Enum):
    IMPURE = "impure"
    NORMAL = "normal"
    PURE = "pure"

class ResourceNode(BaseModel):
    resource_type: str = Field(..., description="Type of resource (e.g., Iron Ore, Copper Ore)", alias="resourceType")
    purity: PurityLevel = Field(..., description="Purity level of the node")
    multiplier: float = Field(..., description="Extraction multiplier for this purity level")
    display_name: Optional[str] = Field(None, description="Display name of the resource", alias="displayName")
    
    class Config:
        populate_by_name = True

