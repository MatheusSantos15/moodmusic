from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from app.database import get_connection
from app.schemas.song import SongCreate

app = FastAPI()

Instrumentator().instrument(app).expose(app)

musicas = []

@app.get("/")
def raiz():
    return {"mensagem": "Music Service Funcionando"}

@app.post("/songs")
def criar_musica(song: SongCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO songs
        (titulo, artista, genero, humor_associado)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (
            song.titulo,
            song.artista,
            song.genero,
            song.humor_associado
        )
    )

    song_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "id": song_id,
        "titulo": song.titulo,
        "artista": song.artista,
        "genero": song.genero,
        "humor_associado": song.humor_associado
    }


@app.get("/songs")
def listar_musicas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM songs")

    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    musicas = []

    for musica in resultados:
        musicas.append({
            "id": musica[0],
            "titulo": musica[1],
            "artista": musica[2],
            "genero": musica[3],
            "humor_associado": musica[4]
        })

    return musicas


@app.get("/songs/{id}")
def buscar_musica(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM songs WHERE id = %s",
        (id,)
    )

    musica = cursor.fetchone()

    cursor.close()
    conn.close()

    if musica:
        return {
            "id": musica[0],
            "titulo": musica[1],
            "artista": musica[2],
            "genero": musica[3],
            "humor_associado": musica[4]
        }

    return {"erro": "Música não encontrada"}

@app.get("/songs/mood/{humor}")
def buscar_por_humor(humor: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM songs
        WHERE humor_associado = %s
        """,
        (humor,)
    )
    
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    musicas = []

    for musica in resultados:
        musicas.append({
            "id": musica[0],
            "titulo": musica[1],
            "artista": musica[2],
            "genero": musica[3],
            "humor_associado": musica[4]
        })

    return musicas