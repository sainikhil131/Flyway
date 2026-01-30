from fastapi import FastAPI
from app.db import get_conn

app = FastAPI()

@app.get("/users")
def get_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
