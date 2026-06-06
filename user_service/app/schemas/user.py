from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str

class User(BaseModel):
    id: int
    nome: str
    humor: str

class MoodUpdate(BaseModel):
    humor: str