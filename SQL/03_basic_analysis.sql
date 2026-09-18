-- 1. Total Customers Count
SELECT COUNT(*) AS total_customers 
FROM customers;

-- 2. Overall Churn Distribution
SELECT Churn, COUNT(*) AS customers 
FROM customers 
GROUP BY Churn;

-- 3. Contract-wise Churn Breakdown
SELECT Contract, Churn, COUNT(*) AS customers 
FROM customers 
GROUP BY Contract, Churn 
ORDER BY Contract, Churn;

-- 4. Internet Service-wise Churn
SELECT InternetService, Churn, COUNT(*) AS customers 
FROM customers 
GROUP BY InternetService, Churn;

-- 5. Average Monthly Charges by Churn Status
SELECT Churn, ROUND(AVG(MonthlyCharges)::numeric, 2) AS avg_monthly_charges 
FROM customers 
GROUP BY Churn;

-- 6. Average Tenure (Months) by Churn Status
SELECT Churn, ROUND(AVG(tenure)::numeric, 2) AS avg_tenure 
FROM customers 
GROUP BY Churn;