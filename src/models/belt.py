from pydantic import BaseModel, Field

class Belt(BaseModel):
    mk: int = Field(..., description="Belt mark version (1 through 6)")
    class_name: str = Field(..., description="Game class name")
    display_name: str = Field(..., description="Display name")
    description: str = Field(..., description="Description")
    speed: float = Field(..., description="Belt speed in items per minute")
    
    class Config:
        populate_by_name = True

