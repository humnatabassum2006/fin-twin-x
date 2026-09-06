import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Calculate Financial Risk Score
df["risk_score"] = (
    (100 - df["debt_score"]) * 0.4
    + (100 - df["savings_score"]) * 0.3
    + (100 - df["emergency_fund_score"]) * 0.3
)

print("Financial Risk Score:")
print(df[[
    "user_id",
    "debt_score",
    "savings_score",
    "emergency_fund_score",
    "risk_score"
]].head())
# Create Risk Category
def classify_risk(score):
    if score < 30:
        return "Low Risk"
    elif score < 60:
        return "Medium Risk"
    else:
        return "High Risk"


df["risk_category"] = df["risk_score"].apply(classify_risk)

print("\nRisk Categories:")
print(df[[
    "user_id",
    "risk_score",
    "risk_category"
]].head(10))
# Count users in each risk category
risk_summary = df["risk_category"].value_counts()

print("\nRisk Summary:")
print(risk_summary)