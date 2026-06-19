from fastapi import FastAPI
import requests
from kafka import KafkaProducer
from prometheus_fastapi_instrumentator import Instrumentator
import json

app = FastAPI()

Instrumentator().instrument(app).expose(app)

producer = KafkaProducer(
    bootstrap_servers="host.docker.internal:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.get("/")
def raiz():
    return {"mensagem": "Recommendation Service funcionando"}

@app.get("/recommendations/{user_id}")
def recomendar(user_id: int):

    resposta_usuario = requests.get(
        f"http://host.docker.internal:8000/internal/users/{user_id}"
    )

    usuario = resposta_usuario.json()

    if"erro" in usuario:
        return usuario
    
    humor = usuario["humor"]

    resposta_musicas = requests.get(
        f"http://host.docker.internal:8001/songs/mood/{humor}"
    )

    musicas = resposta_musicas.json()

    if len(musicas) > 0:

        producer.send(
            "recommendations",
            {
                "user_id": user_id,
                "song_id": musicas[0]["id"]
            }
        )

    return{
    "usuario": usuario["nome"],
    "humor": humor,
    "recomendacoes": musicas
    }