import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn & LTV Dashboard",
    layout="wide"
)

st.title("📊 Customer Churn, LTV & SHAP Insight Dashboard")
st.markdown("FastAPI Predictor Engine ke saath connected interactive UI")

# Sidebar - Customer Profile Input
st.sidebar.header("Customer Profile Input")

tenure = st.sidebar.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=18.0, max_value=150.0, value=70.0)
total_charges = st.sidebar.number_input("Total Charges ($)", min_value=18.0, max_value=9000.0, value=840.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

payload = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract": contract,
    "InternetService": internet_service
}

if st.sidebar.button("Predict Churn & Analyze"):
    try:
        # API Hit to FastAPI Backend
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            res_data = response.json()
            
            col1, col2, col3 = st.columns(3)
            
            churn_prob = res_data["churn_probability"]
            col1.metric("Churn Risk Probability", f"{round(churn_prob * 100, 2)}%")
            
            ltv = res_data["ltv_segmentation"]
            col2.metric("Historic LTV", f"${ltv['historic_ltv']}")
            col3.metric("Expected Future LTV", f"${ltv['expected_future_ltv']}")
            
            st.divider()
            
            # Risk & Action Plan
            st.subheader("🎯 Risk & Retention Recommendation")
            st.info(f"**Customer Segment:** {ltv['customer_segment']}")
            st.warning(f"**Action Required:** {ltv['recommended_action']}")
            
            # SHAP Explainability Drivers
            st.divider()
            st.subheader("🔍 SHAP Top Churn Risk Drivers")
            drivers = res_data["shap_explainability"]["top_churn_risk_drivers"]
            
            for feature, value in drivers.items():
                st.write(f"• **{feature}**: Impact Factor `{value}`")
                
        else:
            st.error("API response failed. Server issue detected.")
            
    except Exception as e:
        st.error(f"FastAPI Server Connection Error: {e}")
        