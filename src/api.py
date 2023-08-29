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
"""
from flask import Flask
from flask_cors import CORS
import os
import pandas as pd
from werkzeug import Response
from flask import request
import pickle

app = Flask(__name__)
CORS(app)


training_data= pd.read_csv(os.path.join("data","auto.mpg.csv"))
#file_to_open = open(os.path.join("data", "models", "baummethoden_lr.pickle", "rb"))


loaded_objects_path = 'data/models/baummethoden_lr.pickle'

with open(loaded_objects_path, 'rb') as objects_file:

    loaded_objects = pickle.load(objects_file)



#trained_model = pickle.load(file_to_open)
#file_to_open.close()

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world2"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return {"hello": "world2"}

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response (training_data.to_json(), mimetype="application/json")

@app.route("/predict", methods=["GET"])
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    #if {zylinder and ps and gewicht and beschleunigung and baujahr}:

    prediction = trained_model.predict([[zylinder, ps, gewicht, beschleunigung, baujahr]])
    print (prediction)

        #return {"result": prediction[0]}

#return Response("Please provide all parameters to get a prediction")

if __name__ == "__main__":
    app.run()
"""

from flask import Flask, request, Response
from flask_cors import CORS
import os
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)

training_data = pd.read_csv(os.path.join("data", "auto.mpg.csv"))

# Load the trained model from the pickle file
loaded_objects_path = 'data/models/baummethoden_lr.pickle'
with open(loaded_objects_path, 'rb') as objects_file:
    trained_model = pickle.load(objects_file)

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world2"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return {"hello": "world2"}

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/predict", methods=["GET"])
def predict():
    zylinder = float(request.args.get("zylinder", 0.0))  # Default value 0.0 if missing
    ps = float(request.args.get("ps", 0.0))
    gewicht = float(request.args.get("gewicht", 0.0))
    beschleunigung = float(request.args.get("beschleunigung", 0.0))
    baujahr = float(request.args.get("baujahr", 0.0))

    prediction = trained_model.predict([[zylinder, ps, gewicht, beschleunigung, baujahr]])
    result = {"result": prediction[0]}

    return result

if __name__ == "__main__":
    app.run()

# Example enter data for predition
# /predict?zylinder=6&ps=200&gewicht=3000&beschleunigung=15&baujahr=1985
