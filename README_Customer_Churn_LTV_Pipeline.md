# Customer Churn & LTV Pipeline

An end-to-end **Customer Churn Prediction and Lifetime Value (LTV) Analytics Pipeline** that combines data cleaning, SQL analysis, exploratory data analysis, machine learning, explainability, FastAPI, and Streamlit to turn customer data into actionable retention decisions.

---

## 📌 Project Overview

Customer churn can significantly affect recurring revenue and long-term customer value. This project builds a complete analytics and ML workflow to:

- **Predict customer churn probability**
- **Estimate historic and expected future LTV**
- **Segment customers by risk/value**
- **Identify important churn risk drivers**
- **Recommend targeted retention actions**
- **Expose predictions through a FastAPI endpoint**
- **Present results in an interactive Streamlit dashboard**

The project is based on the **Telco Customer Churn** dataset.

---

## 🎯 Problem Statement

Businesses often have customer information spread across billing, tenure, contract, and service attributes, but lack a unified system to identify which customers are likely to churn and which at-risk customers are most valuable.

The goal is to build a system that moves from:

**Raw Customer Data → Analytics → Churn Prediction → LTV Estimation → Risk Segmentation → Retention Action**

---

## 💡 Proposed Solution

The project follows a modular, end-to-end pipeline:

1. **Data Ingestion & Verification**
2. **Data Cleaning & Quality Checks**
3. **SQL-Based Analysis**
4. **Exploratory Data Analysis (EDA)**
5. **Feature Preparation**
6. **Machine Learning Modeling**
7. **Model Evaluation & Tuning**
8. **FastAPI Prediction Service**
9. **LTV & Customer Segmentation**
10. **SHAP-Based Explainability**
11. **Streamlit Interactive Dashboard**
12. **Prediction Logging**

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │   Telco Customer Data │
                 └──────────┬───────────┘
                            │
                            ▼
                ┌────────────────────────┐
                │ Data Cleaning & Quality │
                └────────────┬───────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │ EDA + SQL Analysis  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Feature Preparation │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ ML Model Training   │
                 │ Logistic Regression │
                 │ Random Forest       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ FastAPI /predict    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ LTV + Risk + SHAP   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Streamlit Dashboard │
                 └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Data & Analytics
- **Python**
- **Pandas**
- **NumPy**
- **SQL**
- **PostgreSQL**

### Machine Learning
- **Scikit-learn**
- **Logistic Regression**
- **Random Forest**
- **GridSearchCV**
- **Joblib**

### Explainability
- **SHAP**
- Feature importance / risk driver analysis

### Application & API
- **FastAPI**
- **Uvicorn**
- **Streamlit**
- **Requests**

### Version Control
- **Git**
- **GitHub**

---

## 📂 Project Structure

```text
Customer_Churn_LTV_Pipeline/
│
├── Dashboards/
│   ├── dashboard.py
│   └── Customer_Churn_Dashboard.pbix
│
├── Data/
│   ├── Telco-Customer-Churn.csv
│   ├── telco_customer_churn_clean.csv
│   ├── predictions_log.csv
│   └── data_dictionary.md
│
├── Models/
│   ├── churn_random_forest_model.pkl
│   └── scaler.pkl
│
├── Notebooks/
│   ├── 01_data_quality_check.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   └── 04_machine_learning_pipeline.ipynb
│
├── SQL/
│   ├── 01_create_database.sql
│   ├── 02_create_table.sql
│   └── 03_basic_analysis.sql
│
├── SRC/
│   └── app.py
│
├── reports/
│   └── ml_summary.md
│
├── visuals/
│   ├── contract_churn_distribution.png
│   ├── feature_importance.png
│   └── model_roc_comparison.png
│
├── PROJECT_STATUS.md
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

The project uses the **Telco Customer Churn** dataset.

Key customer attributes include:

- **Tenure**
- **Monthly Charges**
- **Total Charges**
- **Contract Type**
- **Internet Service**
- Churn-related customer attributes

The cleaned dataset is stored in:

```text
Data/telco_customer_churn_clean.csv
```

A data dictionary is available at:

```text
Data/data_dictionary.md
```

---

## 🔍 Data Preparation & EDA

The preprocessing workflow includes:

- **Data quality verification**
- **Missing-value handling**
- **Data cleaning**
- **Feature preparation**
- **Exploratory analysis**
- **Churn pattern analysis**
- **SQL-based business analysis**

Important exploratory areas include:

- **Tenure vs Churn**
- **Contract Type vs Churn**
- **Service-related churn patterns**
- **Feature relationships**

---

## 🤖 Machine Learning

Two main classification approaches are included:

### 1. Logistic Regression
Used as a **baseline model** for comparison.

### 2. Random Forest
Used as the primary tree-based classification model.

The workflow includes:

- Feature preprocessing
- Baseline model training
- Random Forest training
- **Hyperparameter tuning with GridSearchCV**
- Model evaluation
- Model serialization

The trained model is stored at:

```text
Models/churn_random_forest_model.pkl
```

The scaler is stored at:

```text
Models/scaler.pkl
```

---

## 📈 Business Metrics: LTV & Segmentation

The API calculates customer value in addition to churn risk.

### Historic LTV

```text
Historic LTV = Tenure × Monthly Charges
```

### Expected Future LTV

The project estimates future customer value using:

- Remaining customer tenure
- Monthly charges
- Predicted churn probability

Customers are then translated into actionable segments such as:

- **High Risk - High Value**
- **Low Risk - High Loyalty**

Retention recommendations are generated based on the risk segment.

---

## 🔎 Explainability

The system exposes top churn risk drivers using a **SHAP-style explainability layer**.

Example drivers include:

- **Contract type**
- **Tenure**
- **Technical support availability**

This helps transform an ML prediction into an understandable business decision.

> Note: The current API returns a curated set of risk drivers in its explainability response.

---

## 🚀 FastAPI Backend

The backend is implemented in:

```text
SRC/app.py
```

### Run the API locally

First install dependencies:

```bash
pip install -r requirements.txt
```

Then start FastAPI:

```bash
uvicorn SRC.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔮 Prediction Endpoint

### Endpoint

```text
POST /predict
```

### Sample Request

```json
{
  "tenure": 12,
  "MonthlyCharges": 69.93,
  "TotalCharges": 840.00,
  "Contract": "One year",
  "InternetService": "Fiber optic"
}
```

### Response Includes

- **Churn prediction**
- **Churn probability**
- **Historic LTV**
- **Expected future LTV**
- **Customer segment**
- **Recommended retention action**
- **Top churn risk drivers**

---

## 🖥️ Streamlit Dashboard

The interactive dashboard is available in:

```text
Dashboards/dashboard.py
```

It allows users to:

- Enter a customer profile
- Adjust **tenure**
- Enter **monthly charges**
- Enter **total charges**
- Select **contract type**
- Select **internet service**
- Trigger a real-time prediction
- View **churn probability**
- View **historic LTV**
- View **future LTV**
- View **customer segment**
- View **recommended retention action**
- Review **risk drivers**

### Run the dashboard locally

```bash
streamlit run Dashboards/dashboard.py
```

The dashboard will normally open at:

```text
http://localhost:8501
```

---

## ⚙️ Local Setup — Step by Step

### Step 1: Clone the repository

```bash
git clone https://github.com/Poonam-yadav22/Customer_Churn_LTV_Pipeline.git
```

### Step 2: Move into the project

```bash
cd Customer_Churn_LTV_Pipeline
```

### Step 3: Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Start FastAPI

```bash
uvicorn SRC.app:app --reload
```

### Step 6: Start Streamlit in a second terminal

```bash
streamlit run Dashboards/dashboard.py
```

### Step 7: Open the dashboard

```text
http://localhost:8501
```

---

## ⚠️ Important: API URL Configuration

The Streamlit dashboard sends prediction requests to FastAPI.

For local development, the dashboard should use:

```python
API_URL = "http://127.0.0.1:8000/predict"
```

For cloud deployment, replace this with the public URL of your deployed FastAPI service:

```python
API_URL = "https://YOUR-BACKEND-URL/predict"
```

The backend and frontend must both be running for real-time prediction to work.

---

## ☁️ Deployment

### Recommended architecture

```text
GitHub
  │
  ├── FastAPI → Render / similar backend host
  │
  └── Streamlit → Streamlit Community Cloud
```

### Backend start command

For a cloud host that provides a `$PORT` environment variable:

```bash
uvicorn SRC.app:app --host 0.0.0.0 --port $PORT
```

### Frontend

Set the Streamlit application entry point to:

```text
Dashboards/dashboard.py
```

Then update `API_URL` in the dashboard to point to the deployed FastAPI endpoint.

---

## 📝 Project Status

### Completed

- [x] Dataset ingestion & verification
- [x] Data cleaning & quality checks
- [x] SQL analysis
- [x] Exploratory Data Analysis
- [x] Baseline ML modeling
- [x] Random Forest modeling
- [x] Hyperparameter tuning
- [x] Model evaluation
- [x] Model serialization
- [x] FastAPI backend
- [x] Streamlit dashboard
- [x] LTV calculation
- [x] Customer segmentation
- [x] Prediction logging
- [x] Explainability layer

### Planned / Future Scope

- [ ] Production-grade deployment
- [ ] Live PostgreSQL integration
- [ ] Model monitoring
- [ ] Data drift detection
- [ ] Batch customer scoring
- [ ] Advanced LTV forecasting
- [ ] Automated retention campaign integration
- [ ] Authentication and role-based access

---

## 📌 Key Business Value

This project is designed to answer three practical questions:

**1. Who is likely to churn?**  
→ Churn probability

**2. Which at-risk customers are most valuable?**  
→ LTV + risk segmentation

**3. What should the business do next?**  
→ Recommended retention action

This makes the pipeline more than a prediction model: it is a **decision-support system for customer retention**.

---

## 👥 Team Contribution

This project includes work across:

- **Data Loading & Quality Checks**
- **Data Cleaning**
- **PostgreSQL / SQL Analysis**
- **EDA**
- **Machine Learning**
- **API Development**
- **Dashboard Development**
- **Documentation & Reporting**

---

## 📚 Key Project Files

| Purpose | File |
|---|---|
| Streamlit Dashboard | `Dashboards/dashboard.py` |
| FastAPI Backend | `SRC/app.py` |
| Trained ML Model | `Models/churn_random_forest_model.pkl` |
| Scaler | `Models/scaler.pkl` |
| Raw Dataset | `Data/Telco-Customer-Churn.csv` |
| Clean Dataset | `Data/telco_customer_churn_clean.csv` |
| Prediction Log | `Data/predictions_log.csv` |
| ML Report | `reports/ml_summary.md` |
| Project Status | `PROJECT_STATUS.md` |

---

## 🔗 Repository

**GitHub:**  
https://github.com/Poonam-yadav22/Customer_Churn_LTV_Pipeline

---

## 👤 Presented / Maintainer

**Poonam Yadav**

---

## ⭐ Future Vision

The long-term goal is to evolve this project into a production-ready **Customer Retention Intelligence Platform** that combines:

**Real-time scoring + LTV forecasting + explainable AI + automated retention workflows**

---

## 📄 License

This project is intended for **academic, learning, and portfolio purposes**.
