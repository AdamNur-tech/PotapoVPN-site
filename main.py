from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
import sqlite3

def get_db():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user'
    )
    """)

    conn.commit()
    conn.close()

init_db()

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-link")
def get_link():
    device = request.args.get("device")

    if device == "android":
        return {"link": "vless://ANDROID_LINK"}
    elif device == "ios":
        return {"link": "vless://IOS_LINK"}
    else:
        return {"error": "unknown device"}
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return {"status": "registered"}
    except:
        return {"error": "user exists"}


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()

    if user:
        return {
            "status": "ok",
            "user_id": user["id"],
            "role": user["role"]
        }
    else:
        return {"error": "invalid login"}


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))