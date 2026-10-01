import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Customer Churn & LTV Engine", layout="wide")

st.title("📊 Customer Churn, LTV & SHAP Dashboard")
st.write("FastAPI Predictor Engine ke saath connected interactive UI")

# Sidebar - Customer Inputs
st.sidebar.header("Customer Profile Input")

tenure = st.sidebar.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=10.0, max_value=200.0, value=70.0)
total_charges = st.sidebar.number_input("Total Charges ($)", min_value=10.0, max_value=10000.0, value=840.0)

contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# API URL
API_URL = "http://127.0.0.1:8000/predict"

if st.sidebar.button("Predict Churn & Analyze"):
    # Payload structured exactly as expected by FastAPI CustomerData schema
    payload = {
        "tenure": int(tenure),
        "MonthlyCharges": float(monthly_charges),
        "TotalCharges": float(total_charges),
        "Contract": str(contract),
        "InternetService": str(internet_service)
    }

    try:
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            res_data = response.json()
            
            st.success("Prediction Successfully Completed!")
            
            # Key Metrics Layout
            col1, col2, col3 = st.columns(3)
            col1.metric("Churn Probability", f"{res_data['churn_probability'] * 100:.2f}%")
            col2.metric("Historic LTV", f"${res_data['ltv_segmentation']['historic_ltv']}")
            col3.metric("Expected Future LTV", f"${res_data['ltv_segmentation']['expected_future_ltv']}")

            st.divider()

            # Customer Segment & Recommended Action
            st.subheader("📌 Customer Segment & Action Recommendation")
            st.info(f"**Segment**: {res_data['ltv_segmentation']['customer_segment']}")
            st.warning(f"**Recommended Action**: {res_data['ltv_segmentation']['recommended_action']}")

            st.divider()

            # SHAP Drivers
            st.subheader("🔍 SHAP Top Churn Risk Drivers")
            drivers = res_data["shap_explainability"]["top_churn_risk_drivers"]
            for feature, value in drivers.items():
                st.write(f"- **{feature}**: Impact Factor `{value}`")

        else:
            st.error(f"API Error ({response.status_code}): {response.text}")

    except Exception as e:
        st.error(f"FastAPI Server Connection Error: {e}")