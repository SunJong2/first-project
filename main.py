from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import requests
import json

app = FastAPI()
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
    return JSONResponse(content=result, media_type="application~/json; charset=utf-8")