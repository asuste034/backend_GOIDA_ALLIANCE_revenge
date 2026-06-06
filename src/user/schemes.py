from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True