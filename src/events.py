from time import time

from flask import request
from flask_socketio import emit

from .extensions import socketio

users = {}

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("new_status")
def handle_status(status):
    emit("status", {"status": status, "ttl": time()}, broadcast=True)
