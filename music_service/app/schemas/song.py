from pydantic import BaseModel

class SongCreate(BaseModel):
    titulo: str
    artista: str
    genero: str
    humor_associado: str

class Song(BaseModel):
    id: int
    titulo: str
    artista: str
    genero: str
    humor_associado: str
