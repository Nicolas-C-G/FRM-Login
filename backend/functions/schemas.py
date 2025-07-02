from pydantic import BaseModel, EmailStr

class CodePayload(BaseModel):
    code: str

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str