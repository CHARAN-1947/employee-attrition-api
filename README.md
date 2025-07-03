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

---

## 🚀 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/CHARAN-1947/employee-attrition-api.git
   cd employee-attrition-api

python -m venv venv
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt


## Usage
1. Train the model:
    python train_model.py

2. Start the API:
    python app.py

3. Test the API
    python test_api.py

## API Endpoint
   POST /predict
    Request Body Example (JSON):
    {
      "Age": 35,
      "Gender": "Male",
      "MonthlyIncome": 6000,
      "OverTime": "Yes",
     ...
    }

   Response Example:
     {
        "prediction": 1,
        "probability_of_attrition": 0.76
     }

## Author
    Charan Teja
    GitHub : CHARAN-1947

