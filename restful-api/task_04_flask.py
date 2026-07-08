#!/usr/bin/python3
"""
Simple Flask API.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users are stored in memory.
# Leave this empty for the checker.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Home endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Return all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user's information."""
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
