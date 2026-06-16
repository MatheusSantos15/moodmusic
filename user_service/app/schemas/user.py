from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    senha: str

class User(BaseModel):
    id: int
    nome: str
    senha: str
    humor: str

class MoodUpdate(BaseModel):
    humor: str

class LoginRequest(BaseModel):
    nome: str
    senha: str