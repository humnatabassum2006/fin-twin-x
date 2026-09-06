import pandas as pd

# User's financial information
monthly_income = 150000
monthly_expenses = 90000
monthly_savings = 60000
debt = 50000

# ML prediction from Step 22
financial_health_score = 55.79

# Risk category from Step 23
if financial_health_score >= 70:
    risk_category = "Low Risk"
elif financial_health_score >= 40:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

# Calculate savings rate
savings_rate = (
    monthly_savings / monthly_income
) * 100

# Calculate debt-to-income ratio
debt_to_income = (
    debt / monthly_income
) * 100

# Create financial report
report = pd.DataFrame({
    "Metric": [
        "Monthly Income",
        "Monthly Expenses",
        "Monthly Savings",
        "Debt",
        "Savings Rate",
        "Debt-to-Income Ratio",
        "Financial Health Score",
        "Risk Category"
    ],
    "Value": [
        monthly_income,
        monthly_expenses,
        monthly_savings,
        debt,
        round(savings_rate, 2),
        round(debt_to_income, 2),
        financial_health_score,
        risk_category
    ]
})

# Display report
print("===== USER FINANCIAL REPORT =====")
print(report.to_string(index=False))