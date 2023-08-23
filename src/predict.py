
"""
import pandas as pd
import pickle

#load trained model
file_to_open = open("data\models\baummethoden_lr.pickle", "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()

# load data that we want predictions for
prediction_data = pd.read_csv("data/prediction-data.csv" , sep=";")

print(trained_model.predict(prediction_data))

"""

import pandas as pd
import pickle

# Load trained model
model_filepath = r"data\models\baummethoden_lr.pickle"

with open(model_filepath, "rb") as model_file:
    trained_model = pickle.load(model_file)

# Load data for predictions
prediction_data_filepath = "data/prediction-data.csv"
prediction_data = pd.read_csv(prediction_data_filepath, sep=";")

# Make predictions
predictions = trained_model.predict(prediction_data)

print(predictions)

