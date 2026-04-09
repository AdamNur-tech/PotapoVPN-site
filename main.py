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

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "VPN backend работает"}

@app.route("/get-link")
def get_link():
    device = request.args.get("device")

    if device == "android":
        return {"link": "vless://ANDROID_LINK"}
    elif device == "ios":
        return {"link": "vless://IOS_LINK"}
    else:
        return {"error": "unknown device"}

app.run(host="0.0.0.0", port=8080)
    cur.execute("SELECT * FROM links WHERE device=? AND used=0 LIMIT 1", (device,))
    row = cur.fetchone()

    if not row:
        return {"error": "no links"}

    cur.execute("UPDATE links SET used=1 WHERE id=?", (row["id"],))
    conn.commit()

    return {"link": row["link"]}