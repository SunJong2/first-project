import sqlite3
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import requests
import json

app = FastAPI()
def init_db():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            searched_at TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/weather/{city}")
def get_weather(city: str):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    data = response.json()
    current = data["current_condition"][0]
    
    result = {
        "city": city,
        "desc": current["weatherDesc"][0]["value"],
        "temp": current["temp_C"],
        "feels_like": current["FeelsLikeC"],
        "humidity": current["humidity"],
        "pressure": current["pressure"],
        "visibility": current["visibility"]
    }
    # DB에 검색 기록 저장
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO history (city, searched_at) VALUES (?, ?)",
        (city, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()
    return JSONResponse(content=result, media_type="application~/json; charset=utf-8")

@app.get("/history")
def get_history():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT city, searched_at FROM history ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    
    return {"history": [{"city": row[0], "searched_at": row[1]} for row in rows]}