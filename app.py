import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Docker CI/CD lab")

@app.route("/health")
def health():
    environment = os.getenv("APP_ENV", "dev")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
