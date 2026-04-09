from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("vpn.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def home():
    return {"status": "VPN backend работает"}

@app.get("/get-link")
def get_link(device: str):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM links WHERE device=? AND used=0 LIMIT 1", (device,))
    row = cur.fetchone()

    if not row:
        return {"error": "no links"}

    cur.execute("UPDATE links SET used=1 WHERE id=?", (row["id"],))
    conn.commit()

    return {"link": row["link"]}