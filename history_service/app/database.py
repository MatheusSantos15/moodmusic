import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="moodmusic",
        user="postgres",
        password="1578648Mm"
    )