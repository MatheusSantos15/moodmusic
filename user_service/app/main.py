from fastapi import FastAPI
from app.database import get_connection
from app.schemas.user import UserCreate, MoodUpdate

app = FastAPI()

usuarios = []



@app.get("/")
def raiz():
    return {"mensagem": "User Service funcionando"}

@app.post("/users")
def criar_usuario(user: UserCreate):

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO users (nome, humor)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (user.nome, "neutro")
    )
    user_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()

    return{
        "id": user_id,
        "nome": user.nome,
        "humor": "neutro"
    }


@app.get("/users")
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY id")

    resultados = cursor.fetchall()
    usuarios = []
    for usuario in resultados:
        usuarios.append({
            "id": usuario[0],
            "nome": usuario[1],
            "humor": usuario[2]
        })

    cursor.close()
    conn.close()
    return usuarios        



@app.get("/users/{id}")
def buscar_usuario(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (id,)
    )

    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    if usuario:
        return {
            "id": usuario[0],
            "nome": usuario[1],
            "humor": usuario[2]
        }
    return {"erro": "Usuário não encontrado"}


@app.put("/users/{id}/mood")
def atualizar_humor(id: int, mood: MoodUpdate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET humor = %s
        WHERE id = %s
        RETURNING id, nome, humor
        """,
        (mood.humor, id)
    )

    usuario = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    if usuario:
        return {
            "id": usuario[0],
            "nome": usuario[1],
            "humor": usuario[2]
        }

    return {"erro": "Usuário não encontrado"}
