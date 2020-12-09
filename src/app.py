from flask import Flask
import os
import socket
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3010)
