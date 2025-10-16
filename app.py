from flask import Flask, render_template, jsonify
from statistics import mean
from data import HOUSES

app = Flask(__name__)

@app.route("/")
def index():
    center = [mean([h["lat"] for h in HOUSES]), mean([h["lon"] for h in HOUSES])]
    # quick log to help debugging when running locally
    app.logger.debug(f"Rendering index with center={center} and {len(HOUSES)} houses")
    return render_template("index.html", center=center)

@app.route("/data.json")
def data():
    return jsonify(HOUSES)

@app.route("/ping")
def ping():
    return "It works ✅"


@app.route('/hello')
def hello():
    # simple health endpoint that returns plain text for quick checks
    return "Hello — Flask is running"

if __name__ == "__main__":
    print("Open http://127.0.0.1:5000 ")
    app.run(debug=True)
