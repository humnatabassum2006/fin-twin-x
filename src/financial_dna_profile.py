import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Select one user
user = df.iloc[0]

# Financial profile
income = user["monthly_income"]
expenses = user["monthly_expenses"]
savings = user["monthly_savings"]
debt = user["debt"]

savings_rate = user["savings_rate"]
debt_to_income = user["debt_to_income"]
emergency_fund = user["emergency_fund_months"]

health_score = user["financial_health_score"]

# Determine financial profile
if savings_rate >= 30:
    savings_profile = "Strong Saver"
elif savings_rate >= 20:
    savings_profile = "Moderate Saver"
else:
    savings_profile = "Low Saver"

if debt_to_income <= 20:
    debt_profile = "Low Debt"
elif debt_to_income <= 40:
    debt_profile = "Moderate Debt"
else:
    debt_profile = "High Debt"

if emergency_fund >= 6:
    emergency_profile = "Excellent Emergency Fund"
elif emergency_fund >= 3:
    emergency_profile = "Good Emergency Fund"
else:
    emergency_profile = "Weak Emergency Fund"

if health_score >= 70:
    health_profile = "Healthy"
elif health_score >= 40:
    health_profile = "Moderate"
else:
    health_profile = "Financially Stressed"

# Display Financial DNA
print("===== FINANCIAL DNA PROFILE =====")

print("User ID:", int(user["user_id"]))

print("\nFinancial Metrics:")
print("Monthly Income:", round(income, 2))
print("Monthly Expenses:", round(expenses, 2))
print("Monthly Savings:", round(savings, 2))
print("Debt:", round(debt, 2))

print("\nFinancial DNA:")
print("Savings Profile:", savings_profile)
print("Debt Profile:", debt_profile)
print("Emergency Fund:", emergency_profile)
print("Overall Health:", health_profile)

print(
    "\nFinancial Health Score:",
    round(health_score, 2)
)