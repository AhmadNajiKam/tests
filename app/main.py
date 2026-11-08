"""Small Flask app used to practice CI/CD pipelines."""

import os

from flask import Flask, jsonify, request


def add(a: float, b: float) -> float:
    return a + b


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=os.getenv("APP_VERSION", "dev"))

    @app.get("/add")
    def add_route():
        try:
            a = float(request.args["a"])
            b = float(request.args["b"])
        except (KeyError, ValueError):
            return jsonify(error="query parameters a and b must be numbers"), 400
        return jsonify(result=add(a, b))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
