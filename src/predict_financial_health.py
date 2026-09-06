import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load ML dataset
df = pd.read_csv("data/ml_dataset.csv")

# Features used by the model
features = [
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "savings_rate",
    "debt_to_income",
    "emergency_fund_months",
    "savings_score",
    "debt_score",
    "emergency_fund_score"
]

# Create training data
X = df[features]
y = df["financial_health_score"]

# Create and train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# New User
# -----------------------------

monthly_income = 150000
monthly_expenses = 90000
monthly_savings = monthly_income - monthly_expenses
debt = 50000

# Calculate features for new user
savings_rate = (
    monthly_savings / monthly_income
) * 100

debt_to_income = (
    debt / monthly_income
) * 100

emergency_fund_months = (
    monthly_savings / monthly_expenses
)

savings_score = (
    min(savings_rate, 50) * 2
)

debt_score = max(
    100 - debt_to_income,
    0
)

emergency_fund_score = (
    min(emergency_fund_months, 6) / 6
) * 100

# Create new user's data
new_user = pd.DataFrame([{
    "monthly_income": monthly_income,
    "monthly_expenses": monthly_expenses,
    "monthly_savings": monthly_savings,
    "debt": debt,
    "savings_rate": savings_rate,
    "debt_to_income": debt_to_income,
    "emergency_fund_months": emergency_fund_months,
    "savings_score": savings_score,
    "debt_score": debt_score,
    "emergency_fund_score": emergency_fund_score
}])

# Predict Financial Health Score
prediction = model.predict(new_user[features])

print("===== New User Financial Health Prediction =====")

print("Monthly Income:", monthly_income)
print("Monthly Expenses:", monthly_expenses)
print("Monthly Savings:", monthly_savings)
print("Debt:", debt)

print(
    "\nPredicted Financial Health Score:",
    round(prediction[0], 2)
)