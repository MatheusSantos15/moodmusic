from fastapi import FastAPI
from app.schemas.user import UserCreate, MoodUpdate

app = FastAPI()

usuarios = []



@app.get("/")
def raiz():
    return {"mensagem": "User Service funcionando"}

@app.post("/users")
def criar_usuario(user: UserCreate):
    
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": user.nome,
        "humor": "neutro"
    }
    usuarios.append(novo_usuario)
    return novo_usuario

@app.get("/users")
def listar_usuarios():
    return usuarios

@app.get("/users/{id}")
def buscar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return {"erro": "Usuário não encontrado"}

@app.put("/users/{id}/mood")
def atualizar_humor(id: int, mood: MoodUpdate):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["humor"] = mood.humor
            return usuario
    return {"erro": "Usuário não encontrado"}
