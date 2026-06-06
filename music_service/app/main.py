from fastapi import FastAPI
from app.schemas.song import SongCreate

app = FastAPI()

musicas = []

@app.get("/")
def raiz():
    return {"mensagem": "Music Service Funcionando"}

@app.post("/songs")
def criar_musica(song: SongCreate):
    nova_musica = {
        "id": len(musicas) + 1,
        "titulo": song.titulo,
        "artista": song.artista,
        "genero": song.genero,
        "humor_associado": song.humor_associado
    }
    musicas.append(nova_musica)
    return nova_musica