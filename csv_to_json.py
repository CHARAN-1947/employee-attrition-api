# csv_to_json.py  
# -------------------------------------------------
# It will read WA_Fn-UseC_-HR-Employee-Attrition.csv (same folder)
# and write WA_Fn-UseC_-HR-Employee-Attrition.json.

import pandas as pd
import json
from pathlib import Path

# 1. File paths
csv_path  = Path("WA_Fn-UseC_-HR-Employee-Attrition.csv")   # your dataset
json_path = csv_path.with_suffix(".json")                   # output = .json

# 2. Load CSV
if not csv_path.exists():
    raise FileNotFoundError(f"❌ File not found: {csv_path}")

df = pd.read_csv(csv_path)

# 3. Convert to list-of-dicts and save
records = df.to_dict(orient="records")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

print(f"✅ Converted {csv_path.name} → {json_path.name}  ({len(records)} rows)")
