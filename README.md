# Employee Attrition Prediction API

A production‑style pipeline that trains a Random Forest model on IBM’s HR data
and serves predictions through a Flask REST API.

## Project structure
.
├── train_model.py      # data prep + model training + export
├── csv_to_json.py      # utility: CSV → JSON
├── app.py              # Flask API for real‑time predictions
├── test_api.py         # smoke‑test script for /predict endpoint
├── model/              # saved model + columns (created by train_model.py)
├── requirements.txt
└── README.md

