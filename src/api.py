"""

from flask import flask #, Response, request
from flask_cors import CORS
#import os
#import pandas as pd
#import pickle
app = Flask(__name__)

CORS(app)

@app.routet ("/", methods=["GET"])
def index():
    return {"hello": "world"}

"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world2"}

if __name__ == "__main__":
    app.run()
