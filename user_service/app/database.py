import psycopg2

def get_connection():
    return psycopg2.connect(
        host="host.docker.internal",
        database="moodmusic",
        user="postgres",
        password="1578648Mm"
    )

if __name__ == "__main__":
    conn = get_connection()
    print("Conectado com sucesso!")
    conn.close()