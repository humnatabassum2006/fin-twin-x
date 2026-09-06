import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Sort users by Financial Health Score
top_users = df.sort_values(
    by="financial_health_score",
    ascending=False
).head(10)

print("Top 10 Financially Healthy Users:")
print(top_users[[
    "user_id",
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "financial_health_score"
]])