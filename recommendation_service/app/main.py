from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Recommendation Service funcionando"}

@app.get("/recommendations/{user_id}")
def recomendar(user_id: int):

    resposta_usuario = requests.get(
        f"http://127.0.0.1:8000/internal/users/{user_id}"
    )

    usuario = resposta_usuario.json()

    if"erro" in usuario:
        return usuario
    
    humor = usuario["humor"]

    resposta_musicas = requests.get(
        f"http://127.0.0.1:8001/songs/mood/{humor}"
    )

    musicas = resposta_musicas.json()

    if len(musicas) > 0:
        requests.post(
            "http://127.0.0.1:8002/history",
            json={
                "user_id": user_id,
                "song_id": musicas[0]["id"]
            }
        )

    return{
    "usuario": usuario["nome"],
    "humor": humor,
    "recomendacoes": musicas
    }