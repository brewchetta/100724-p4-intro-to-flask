#!/usr/bin/env python3

from flask import make_response, jsonify
from config import app

@app.get('/')
def index():
    return make_response( "<h1>Hello World</h1>" )

if __name__ == '__main__':
    app.run(port=5555, debug=True)
