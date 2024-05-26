from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger #swagger will be an API and will automaticall generate the UI

app = Flask(__name__)
Swagger(app)

pickle_in = open("C:/Users/user/Docker/classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Welcome all"

@app.route("/predict",methods=["Get"])
def predict_note_authentication():

    '''Let's Authenticate the bank note.
    This is usingdocstrings for specifications.
    ---
    parameters:
        - name: varience
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
          200:
            descriptin: The output value
    '''
    varience = request.args.get("varience")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[varience, skewness, curtosis, entropy]])
    return "Hello the anser is " + str(prediction)

@app.route("/predict_file",methods=["POST"])
def predict_note_file():
    '''Let's Authenticate the bank note.
    This is usingdocstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
          200:
            descriptin: The output value
    '''
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
  
    return "The predicted value for the csv is " + str(list(prediction))

if __name__ == "__main__":
    app.run()