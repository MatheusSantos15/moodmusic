from fastapi import FastAPI
from app.schemas.history import HistoryCreate

app = FastAPI()

historicos = []

@app.get("/")
def raiz():
    return{"mensagem": "History Service funcionando"}

@app.post("/history")
def criar_historico(history: HistoryCreate):
    novo_historico = {
        "id": len(historicos) + 1,
        "user_id": history.user_id,
        "song_id": history.song_id
    }

    historicos.append(novo_historico)
    return novo_historico

@app.get("/history")
def listar_historicos():
    return historicos

@app.get("/history/{id}")
def buscar_historicos(id: int):
    for historico in historicos:
        if historico["id"] == id:
            return historico
    return {"erro": "Histórico não encontrado"}