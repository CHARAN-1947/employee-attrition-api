"""
Quick smoke-test for the Flask /predict API.
"""

import json
import time
import requests

URL = "http://127.0.0.1:5000/predict"  

employees = json.load(open("WA_Fn-UseC_-HR-Employee-Attrition.json"))

# ── 1. Loop through & call API ───────────────────────────────────────────
for idx, emp in enumerate(employees[:10],1):
    resp = requests.post(URL, json=emp, timeout=5)
    resp.raise_for_status()                     # crash fast on HTTP errors
    result = resp.json()

    print(f"\nEmployee {idx}")
    print(json.dumps(result, indent=2))

    if result["probability_of_attrition"] > 0.5:
        print("⚠️  High attrition risk!")
    else:
        print("✅  Low attrition risk.")

    time.sleep(0.25)                            # gentle pause; optional
