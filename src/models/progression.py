from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class Milestone(BaseModel):
    class_name: str = Field(..., description="Game class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    description: str = Field(..., description="Description")
    tier: int = Field(..., description="Tier number")
    phase: int = Field(..., description="Phase number")
    cost: Optional[List[Dict[str, Any]]] = Field(None, description="Cost items for unlocking", alias="cost")
    
    class Config:
        populate_by_name = True

class Unlock(BaseModel):
    class_name: str = Field(..., description="Item or building class name", alias="className")
    display_name: str = Field(..., description="Display name", alias="displayName")
    unlock_type: str = Field(..., description="Type of unlock (building, item, recipe)", alias="unlockType")
    tier: Optional[int] = Field(None, description="Tier when unlocked")
    milestone: Optional[str] = Field(None, description="Milestone that unlocks this")
    mam_research: Optional[str] = Field(None, description="MAM research that unlocks this", alias="mamResearch")
    
    class Config:
        populate_by_name = True

