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
    return {"hello": "world2"}

"""

from flask import Flask
from flask_cors import CORS
import os
import pandas as pd
from werkzeug import Response

app = Flask(__name__)
CORS(app)


training_data= pd.read_csv(os.path.join("data","auto.mpg.csv"))

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world2"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return {"hello": "world2"}

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response (training_data.to_json(), mimetype="application/json")


if __name__ == "__main__":
    app.run()
