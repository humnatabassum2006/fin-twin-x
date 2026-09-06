import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Calculate Financial Risk Score
df["risk_score"] = (
    (100 - df["debt_score"]) * 0.4
    + (100 - df["savings_score"]) * 0.3
    + (100 - df["emergency_fund_score"]) * 0.3
)

# Create Risk Category
def classify_risk(score):
    if score < 30:
        return "Low Risk"
    elif score < 60:
        return "Medium Risk"
    else:
        return "High Risk"

df["risk_category"] = df["risk_score"].apply(classify_risk)

# Select High Risk Users
high_risk_users = df[
    df["risk_category"] == "High Risk"
]

# Sort by highest risk
high_risk_users = high_risk_users.sort_values(
    by="risk_score",
    ascending=False
)

# Show Top 10 High Risk Users
print("Top 10 High Risk Users:")
print(high_risk_users[[
    "user_id",
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "risk_score",
    "risk_category"
]].head(10))