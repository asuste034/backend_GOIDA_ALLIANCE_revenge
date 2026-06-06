from pydantic import BaseModel

class UserLogin(BaseModel):
    name: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
