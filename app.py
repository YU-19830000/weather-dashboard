from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = "d3fd0dc57e3e870f99fe99b883435b85"  # ← ご自身のキーに置き換えてください

def get_weather_by_coords(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return {"city": "不明", "description": "取得失敗", "temperature": "―"}
    return {
        "city": res["name"],
        "description": res["weather"][0]["description"],
        "temperature": res["main"]["temp"]
    }

@app.route("/")
def index():
    lat = 35.3983   # 各務原市
    lon = 136.8486
    weather = get_weather_by_coords(lat, lon)
    return render_template("dashboard.html", lat=lat, lon=lon, weather=weather)

@app.route("/weather_by_coords", methods=["POST"])
def weather_by_coords():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    return jsonify(get_weather_by_coords(lat, lon))

if __name__ == "__main__":
    app.run(debug=True)
