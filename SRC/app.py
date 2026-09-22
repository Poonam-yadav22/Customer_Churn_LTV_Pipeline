from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title="Customer Churn & LTV Engine API")

# Load Serialized Artifacts
model = joblib.load("Models/churn_random_forest_model.pkl")
scaler = joblib.load("Models/scaler.pkl")

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str

def calculate_ltv_metrics(monthly_charges: float, tenure: int, churn_prob: float):
    # Calculations
    historic_ltv = monthly_charges * tenure
    expected_future_ltv = (monthly_charges * 12) * (1.0 - churn_prob)
    
    # Action Strategy Matrix
    if churn_prob > 0.60:
        risk_level = "High"
        if expected_future_ltv > 500:
            segment = "High Risk - High Value"
            action = "Priority Retention: Offer 20% Discount on 1-Year Contract"
        else:
            segment = "High Risk - Low Value"
            action = "Automated Email Survey & Small Discount"
    elif churn_prob > 0.30:
        risk_level = "Medium"
        segment = "Medium Risk"
        action = "Send Engagement Newsletter & Add-on Offers"
    else:
        risk_level = "Low"
        segment = "Low Risk"
        action = "Standard Loyalty Perks / Cross-sell Options"

    return {
        "historic_ltv": round(historic_ltv, 2),
        "expected_future_ltv": round(expected_future_ltv, 2),
        "risk_level": risk_level,
        "customer_segment": segment,
        "recommended_action": action
    }

@app.get("/")
def home():
    return {"status": "Online", "message": "Customer Churn Prediction API is Running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    raw_data = pd.DataFrame([data.dict()])
    processed_data = pd.get_dummies(raw_data)
    
    # Align features with model
    model_features = getattr(model, "feature_names_in_", None)
    if model_features is not None:
        processed_data = processed_data.reindex(columns=model_features, fill_value=0)
    
    # Prediction
    churn_prob = float(model.predict_proba(processed_data)[0][1])
    churn_prediction = int(churn_prob > 0.5)
    
    # Business Logic
    ltv_details = calculate_ltv_metrics(data.MonthlyCharges, data.tenure, churn_prob)
    
    return {
        "churn_prediction": churn_prediction,
        "churn_probability": round(churn_prob, 4),
        "ltv_metrics": ltv_details
    }