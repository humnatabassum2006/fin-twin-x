import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Normal Financial Health Score
df["normal_health_score"] = df["financial_health_score"]

# 20% income reduction
df["stressed_income"] = df["monthly_income"] * 0.80

# Recalculate savings
df["stressed_savings"] = (
    df["stressed_income"] - df["monthly_expenses"]
).clip(lower=0)

# Recalculate Savings Score
df["stressed_savings_rate"] = (
    df["stressed_savings"] / df["stressed_income"]
) * 100

df["stressed_savings_score"] = (
    df["stressed_savings_rate"].clip(0, 50) * 2
)

# Recalculate Emergency Fund Score
df["stressed_emergency_fund_months"] = (
    df["stressed_savings"] / df["monthly_expenses"]
)

df["stressed_emergency_fund_score"] = (
    df["stressed_emergency_fund_months"].clip(0, 6) / 6
) * 100

# Debt Score remains unchanged
df["stressed_debt_score"] = df["debt_score"]

# Stressed Financial Health Score
df["stressed_health_score"] = (
    df["stressed_savings_score"] * 0.4
    + df["stressed_debt_score"] * 0.3
    + df["stressed_emergency_fund_score"] * 0.3
)

# Calculate health score decrease
df["health_score_change"] = (
    df["normal_health_score"]
    - df["stressed_health_score"]
)

# Summary calculations
total_users = len(df)

average_drop = df["health_score_change"].mean()
maximum_drop = df["health_score_change"].max()

significant_drop_users = (
    df["health_score_change"] > 10
).sum()

significant_drop_percentage = (
    significant_drop_users / total_users
) * 100

# Display summary
print("===== Stress Test Impact Summary =====")

print("Total Users:", total_users)

print(
    "Average Health Score Drop:",
    round(average_drop, 2)
)

print(
    "Maximum Health Score Drop:",
    round(maximum_drop, 2)
)

print(
    "Users with Significant Drop:",
    significant_drop_users
)

print(
    "Significant Drop Percentage:",
    round(significant_drop_percentage, 2),
    "%"
)