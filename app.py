from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_weather_by_coords(lat, lon):
    api_key = 'd3fd0dc57e3e870f99fe99b883435b85'
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=ja"
    res = requests.get(url).json()
    print(f"🌐 リクエストURL: {url}")
    print(f"📦 APIレスポンス: {res}")

    if res.get("cod") != 200:
        return {"city": "不明", "description": "取得失敗", "temperature": "―"}

    return {
        "city": res["name"],
        "description": res["weather"][0]["description"],
        "temperature": res["main"]["temp"]
    }

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/weather_by_coords", methods=["POST"])
def weather_by_coords():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    return jsonify(get_weather_by_coords(lat, lon))

if __name__ == '__main__':
    app.run(debug=True)
