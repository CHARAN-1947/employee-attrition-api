import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the dataset

data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Display basic information about the dataset
print("Dataset Information:\n")
print(data.info())
print("\nSummary Statistics:\n")
print(data.describe())
print("\nFirst Few Rows:\n")
print(data.head())

# Check for missing values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Explore the target variable 'Attrition'
sns.countplot(data=data, x='Attrition')
plt.title('Employee Attrition Distribution')
plt.show()
print("the first plot was completed and moving to the second slot")
# Convert categorical variables into dummy/indicator variables
data = pd.get_dummies(data, drop_first=True)

# Define the features (X) and target (y)
X = data.drop('Attrition_Yes', axis=1)
y = data['Attrition_Yes']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nAccuracy Score:\n")
print(accuracy_score(y_test, y_pred))

# Feature Importance
importances = pd.DataFrame({'Feature': X.columns, 'Importance': clf.feature_importances_})
importances = importances.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=importances.head(10))
plt.title('Top 10 Important Features for Employee Attrition')
plt.show()

import joblib
import json
import os
os.makedirs("model",exist_ok=True)
joblib.dump(clf,"model/model.pkl")
with open("model/columns.json",'w') as f:
    json.dump(list(X.columns),f)
print("Model and columns saved.")