import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# -----------------------------
# NORMAL FINANCIAL HEALTH
# -----------------------------

normal_health = df["financial_health_score"]

# -----------------------------
# STRESS SCENARIO
# Income decreases by 20%
# -----------------------------

df["stressed_income"] = df["monthly_income"] * 0.80

# Recalculate savings
df["stressed_savings"] = (
    df["stressed_income"] - df["monthly_expenses"]
)

# Savings cannot be negative
df["stressed_savings"] = df["stressed_savings"].clip(lower=0)

# -----------------------------
# STRESSED FINANCIAL SCORES
# -----------------------------

df["stressed_savings_rate"] = (
    df["stressed_savings"] / df["stressed_income"]
) * 100

df["stressed_savings_score"] = (
    df["stressed_savings_rate"].clip(0, 50) * 2
)

df["stressed_emergency_fund_months"] = (
    df["stressed_savings"] / df["monthly_expenses"]
)

df["stressed_emergency_fund_score"] = (
    df["stressed_emergency_fund_months"].clip(0, 6) / 6
) * 100

# Debt score remains the same because
# this scenario only changes income
df["stressed_debt_score"] = df["debt_score"]

# Calculate stressed Financial Health Score
df["stressed_health_score"] = (
    df["stressed_savings_score"] * 0.4
    + df["stressed_debt_score"] * 0.3
    + df["stressed_emergency_fund_score"] * 0.3
)

# Calculate health score decrease
df["health_score_change"] = (
    df["financial_health_score"]
    - df["stressed_health_score"]
)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("===== 20% Income Reduction Stress Test =====")

print(df[[
    "user_id",
    "financial_health_score",
    "stressed_health_score",
    "health_score_change"
]].head(10))