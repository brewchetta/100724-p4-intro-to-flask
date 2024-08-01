#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.json.compact = False
# javascript object notation

CORS(app)