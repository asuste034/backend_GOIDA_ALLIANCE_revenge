from typing import Optional
from pydantic import BaseModel, Json

class Event(BaseModel):
    title: str
    type : str
    block : Optional[str]
    emergency_block : Optional[str]

class EventResponse(BaseModel):
    id : int
    title: str
    type: str
    block: Optional[str]
    emergency_block: Optional[str]
    class Config:
        from_attributes = True

class Block(BaseModel):
    title: str
    content: str
    date: Optional[str] = None
    image: Optional[str] = None

class EmergencyBlock(BaseModel):
    text: str
    timeout : str