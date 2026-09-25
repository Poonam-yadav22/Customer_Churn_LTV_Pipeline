from fastapi import FastAPI
import joblib
import pandas as pd
import shap
from pydantic import BaseModel

app = FastAPI(title="Customer Churn, LTV & SHAP Engine API")

# Load Models
model = joblib.load("Models/churn_random_forest_model.pkl")
scaler = joblib.load("Models/scaler.pkl")

# Initialize SHAP TreeExplainer
explainer = shap.TreeExplainer(model)

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str

def calculate_ltv_and_segment(monthly_charges: float, tenure: int, churn_prob: float):
    historic_ltv = monthly_charges * tenure
    expected_future_ltv = (monthly_charges * 12) * (1.0 - churn_prob)
    
    if churn_prob > 0.60:
        risk_level = "High Risk"
        if expected_future_ltv > 500:
            segment = "High Risk - High Value (VIP)"
            action = "Priority Retention: Offer 20% Discount + Direct Account Manager Reachout"
        else:
            segment = "High Risk - Low Value"
            action = "Automated Exit Survey & Standard Discount Voucher"
    elif churn_prob > 0.30:
        risk_level = "Medium Risk"
        if expected_future_ltv > 500:
            segment = "Medium Risk - High Value"
            action = "Proactive Upsell Discount & Loyalty Perks"
        else:
            segment = "Medium Risk - Low Value"
            action = "Engagement Newsletter & Feature Onboarding Guide"
    else:
        risk_level = "Low Risk"
        segment = "Low Risk - High Loyalty"
        action = "Standard Loyalty Perks & Cross-sell Add-ons"

    return {
        "historic_ltv": round(historic_ltv, 2),
        "expected_future_ltv": round(expected_future_ltv, 2),
        "risk_level": risk_level,
        "customer_segment": segment,
        "recommended_action": action
    }

@app.get("/")
def home():
    return {"status": "Online", "message": "Customer Churn, LTV & SHAP Engine API is Running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    raw_data = pd.DataFrame([data.dict()])
    processed_data = pd.get_dummies(raw_data)
    
    model_features = getattr(model, "feature_names_in_", None)
    if model_features is not None:
        processed_data = processed_data.reindex(columns=model_features, fill_value=0)
    
    # 1. Churn Prediction
    churn_prob = float(model.predict_proba(processed_data)[0][1])
    churn_prediction = int(churn_prob > 0.5)
    
    # 2. LTV & Customer Segmentation
    ltv_details = calculate_ltv_and_segment(data.MonthlyCharges, data.tenure, churn_prob)
    
    # 3. SHAP Feature Explainability
    raw_shap = explainer.shap_values(processed_data)
    
    if isinstance(raw_shap, list):
        vals = raw_shap[1][0]
    elif len(raw_shap.shape) == 3:
        vals = raw_shap[0, :, 1]
    else:
        vals = raw_shap[0]

    feature_impacts = pd.Series(vals, index=processed_data.columns)
    top_drivers = feature_impacts.sort_values(ascending=False).head(3).to_dict()
    formatted_drivers = {feat: round(float(val), 4) for feat, val in top_drivers.items()}
    
    return {
        "churn_prediction": churn_prediction,
        "churn_probability": round(churn_prob, 4),
        "ltv_segmentation": ltv_details,
        "shap_explainability": {
            "top_churn_risk_drivers": formatted_drivers
        }
    }