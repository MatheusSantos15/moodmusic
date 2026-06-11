from fastapi import FastAPI, HTTPException
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

@app.get("/songs")
def listar_musicas():
    return musicas

@app.get("/songs/{song_id}")
def buscar_musica(song_id: int):
    for musica in musicas:
        if musica["id"] == song_id:
            return musica
        
    raise HTTPException(
        status_code=404,
        detail = "Música não encontrada"
    )

