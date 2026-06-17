from fastapi import FastAPI
from app.database import get_connection
from app.schemas.history import HistoryCreate
from kafka import KafkaConsumer
import json
import threading

app = FastAPI()

def consumir_recomendacoes():

    consumer = KafkaConsumer(
        "recommendations",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )

    for mensagem in consumer:
        
        dados = mensagem.value

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO history
            (user_id, song_id)
            VALUES (%s, %s)
            """,
            (
                dados["user_id"],
                dados["song_id"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print(f"Histórico salvo via Kafka: {dados}")

threading.Thread(
    target=consumir_recomendacoes,
    daemon=True
).start()

historicos = []

@app.get("/")
def raiz():
    return{"mensagem": "History Service funcionando"}

@app.post("/history")
def criar_historico(history: HistoryCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history
        (user_id, song_id)
        VALUES (%s, %s)
        RETURNING id
        """,
        (
            history.user_id,
            history.song_id
        )
    )

    history_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "id": history_id,
        "user_id": history.user_id,
        "song_id": history.song_id
    }



@app.get("/history")
def listar_historicos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history")

    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    historicos = []

    for historico in resultados:
        historicos.append({
            "id": historico[0],
            "user_id": historico[1],
            "song_id": historico[2]
        })

    return historicos



@app.get("/history/{id}")
def buscar_historico(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history WHERE id = %s",
        (id,)
    )

    historico = cursor.fetchone()

    cursor.close()
    conn.close()

    if historico:
        return {
            "id": historico[0],
            "user_id": historico[1],
            "song_id": historico[2]
        }

    return {"erro": "Histórico não encontrado"}