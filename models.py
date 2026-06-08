from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str