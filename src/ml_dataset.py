import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Select features for Machine Learning
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

# Create ML dataset
ml_df = df[[
    "user_id",
    *features,
    "financial_health_score"
]]

# Save ML-ready dataset
ml_df.to_csv("data/ml_dataset.csv", index=False)

# Display information
print("===== ML Dataset Created =====")
print("Rows:", len(ml_df))
print("Columns:", len(ml_df.columns))

print("\nML Features:")
print(features)

print("\nFirst 5 Rows:")
print(ml_df.head())