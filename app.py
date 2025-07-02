from flask import Flask, request, jsonify
import joblib
import pandas as pd
import json
model = joblib.load("model/model.pkl")
with open("model/columns.json") as f:
    columns = json.load(f)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Employee Attrition Prediction API!"
@app.route("/predict",methods = ["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    df = pd.get_dummies(df,drop_first = True)
    df = df.reindex(columns = columns, fill_value = 0)
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    return jsonify({
        "prediction": int(pred),
        "probability_of_attrition": round(prob,4)
    })

if __name__ == "__main__":
    app.run(debug = True)