import os
import socket
from flask import Flask
from redis import Redis

app = Flask(__name__)
# Connects to Redis running inside the same Pod (sidecar or same network)
redis = Redis(host='localhost', port=6379, db=0)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception as e:
        count = f"Error connecting to Redis: {e}"
        
    pod_name = socket.gethostname()
    return f"<h3>Hello! This page has been viewed {count} times.</h3><br><b>Served by Pod:</b> {pod_name}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

