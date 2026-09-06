import pandas as pd

# Load financial data
df = pd.read_csv("data/users.csv")

# Calculate savings rate
df["savings_rate"] = (
    df["monthly_savings"] / df["monthly_income"]
) * 100

print(df[[
    "user_id",
    "monthly_income",
    "monthly_savings",
    "savings_rate"
]].head())
# Calculate Debt-to-Income Ratio
df["debt_to_income"] = (
    df["debt"] / df["monthly_income"]
) * 100

print("\nDebt-to-Income Ratio:")
print(df[[
    "user_id",
    "monthly_income",
    "debt",
    "debt_to_income"
]].head())
# Calculate Emergency Fund Months
df["emergency_fund_months"] = (
    df["emergency_fund_savings"] / df["monthly_expenses"]
)

print("\nEmergency Fund Months:")
print(df[[
    "user_id",
    "monthly_expenses",
    "monthly_savings",
    "emergency_fund_months"
]].head())
# Save feature-engineered dataset
df.to_csv("data/users_with_features.csv", index=False)

print("\nFeature dataset saved successfully!")
# Calculate Savings Score
df["savings_score"] = df["savings_rate"].clip(0, 50) * 2

print("\nSavings Score:")
print(df[[
    "user_id",
    "savings_rate",
    "savings_score"
]].head())
# Calculate Debt Score
df["debt_score"] = (100 - df["debt_to_income"]).clip(0, 100)

print("\nDebt Score:")
print(df[[
    "user_id",
    "debt_to_income",
    "debt_score"
]].head())
# Calculate Emergency Fund Score
df["emergency_fund_score"] = (
    df["emergency_fund_months"].clip(0, 6) / 6
) * 100

print("\nEmergency Fund Score:")
print(df[[
    "user_id",
    "emergency_fund_months",
    "emergency_fund_score"
]].head())
# Calculate Overall Financial Health Score
df["financial_health_score"] = (
    df["savings_score"] * 0.4
    + df["debt_score"] * 0.3
    + df["emergency_fund_score"] * 0.3
)

print("\nFinancial Health Score:")
print(df[[
    "user_id",
    "savings_score",
    "debt_score",
    "emergency_fund_score",
    "financial_health_score"
]].head())
# Save final Financial DNA dataset
df.to_csv("data/financial_dna.csv", index=False)

print("\nFinancial DNA dataset saved successfully!")