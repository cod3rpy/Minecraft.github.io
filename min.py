from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)
STATUS_API = "https://status.mojang.com/check"

def fetch_status():
    try:
        response = requests.get(STATUS_API)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка загрузки статуса: {e}")
        return []

@app.route("/")
def index():
    statuses = fetch_status()
    return render_template("index.html", statuses=statuses)

@app.route("/status")
def get_status():
    statuses = fetch_status()
    return jsonify(statuses)

if __name__ == "__main__":
    app.run(debug=True)
