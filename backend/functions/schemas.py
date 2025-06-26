from pydantic import BaseModel

class CodePayload(BaseModel):
    code: str

class LoginRequest(BaseModel):
    username: str
    password: str