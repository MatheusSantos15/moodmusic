from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from app.database import get_connection
from app.schemas.user import UserCreate, MoodUpdate,LoginRequest


app = FastAPI()

usuarios = []

SECRET_KEY = "moodmusic123456"
ALGORITHM = "HS256"

security = HTTPBearer()

def create_access_token(data: dict):

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm = ALGORITHM
    )
    return token

def verify_token(token: str):

    payload =jwt.decode(
        token,
        SECRET_KEY,
        algorithms = [ALGORITHM]
    )

    return payload

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    print("TOKEN:", token)

    payload = verify_token(token)

    return payload

@app.get("/")
def raiz():
    return {"mensagem": "User Service funcionando"}

@app.post("/users")
def criar_usuario(user: UserCreate):

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO users (nome, humor, senha)
        VALUES (%s, %s, %s)
        RETURNING id;
        """,
        (user.nome, "neutro", user.senha)
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

@app.post("/login")
def login(user: LoginRequest):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, nome
        FROM users
        WHERE nome = %s
        AND senha = %s
        """,
        (user.nome, user.senha)
    )

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario is None:
        return {
            "erro": "Usuário ou senha inválidos"
        }
    token = create_access_token(
        {
            "user_id": usuario[0],
            "nome": usuario[1]
        }
    )
    return {
        "access_token": token
    }

@app.get("/token-test")
def token_test(token: str):

    payload = verify_token(token)

    return{
        "payload": payload
    }

@app.get("/users")
def listar_usuarios(
    current_user = Depends(get_current_user)
):
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
def buscar_usuario(
    id: int,
    current_user = Depends(get_current_user)
):
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
def atualizar_humor(
    id: int,
    mood: MoodUpdate,
    current_user = Depends(get_current_user)
):

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

@app.get("/internal/users/{id}")
def buscar_usuario_interno(id: int):
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
    
    return{
        "erro": "Usuário não encontrado"
    }