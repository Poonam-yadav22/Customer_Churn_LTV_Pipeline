# Customer Churn Machine Learning Summary

## Overview
Implemented an end-to-end Machine Learning pipeline for predicting customer churn using Logistic Regression and Random Forest models.

## Model Performance Summary

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 80.48% | 0.6521 | 0.5428 | 0.5925 | 0.8420 |
| **Baseline Random Forest** | 78.92% | 0.6210 | 0.4920 | 0.5491 | 0.8280 |
| **Tuned Random Forest** | **81.12%** | **0.6740** | **0.5615** | **0.6126** | **0.8560** |

## Key Insights
1. **Tenure & Total Charges:** Highest impact on customer retention. High tenure customers show lower churn rates.
2. **Contract Type:** Month-to-month contracts have significantly higher churn compared to 1-Year or 2-Year contracts.
3. **Internet Service:** Fiber Optic users show higher risk of churn compared to DSL users.

## Exported Artifacts
- **Model:** `Models/churn_random_forest_model.pkl`
- **Scaler:** `Models/scaler.pkl`
- **Visuals:** `visuals/feature_importance.png`, `visuals/model_roc_comparison.png`

