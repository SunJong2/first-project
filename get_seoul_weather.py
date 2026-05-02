import requests

def get_seoul_weather():
    response = requests.get("https://wttr.in/Seoul?format=j1")
    data = response.json()

    current = data["current_condition"][0]

    temp = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    pressure = current["pressure"]
    visibility = current["visibility"]
    desc = current["weatherDesc"][0]["value"]

    print(f"=== 서울 현재 날씨 ===")
    print(f"날씨: {desc}")
    print(f"온도: {temp}°C (체감 {feels_like}°C)")
    print(f"습도: {humidity}%")
    print(f"기압: {pressure}hPa")
    print(f"시야: {visibility}km")

get_seoul_weather()



