from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open("C:/Users/user/Docker/classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Welcome all"

@app.route("/predict")
def predict_note_authentication():
    varience = request.args.get("varience")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[varience, skewness, curtosis, entropy]])
    return "The predicted value is " + str(prediction)

@app.route("/predict_file",methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
  
    return "The predicted value for the csv is " + str(list(prediction))

if __name__ == "__main__":
    app.run()