import pandas as pd


# =========================================================
# LOAD FINANCIAL DNA DATA
# =========================================================

df = pd.read_csv("data/financial_dna_profiles.csv")


# =========================================================
# SELECT A USER
# =========================================================

selected_user = df.iloc[0]


# =========================================================
# FINANCIAL HEALTH SCORE COMPONENTS
# =========================================================

savings_contribution = (
    selected_user["savings_score"] * 0.4
)

debt_contribution = (
    selected_user["debt_score"] * 0.3
)

emergency_contribution = (
    selected_user["emergency_fund_score"] * 0.3
)


# =========================================================
# DISPLAY EXPLANATION
# =========================================================

print("========================================")
print("       FINANCIAL HEALTH EXPLANATION")
print("========================================")

print(
    "User ID:",
    selected_user["user_id"]
)

print(
    "Financial Health Score:",
    round(
        selected_user["financial_health_score"],
        2
    )
)

print("\nScore Contributions:")

print(
    "Savings Contribution:",
    round(
        savings_contribution,
        2
    )
)

print(
    "Debt Contribution:",
    round(
        debt_contribution,
        2
    )
)

print(
    "Emergency Fund Contribution:",
    round(
        emergency_contribution,
        2
    )
)


# =========================================================
# MOST IMPORTANT FACTOR
# =========================================================

contributions = {
    "Savings": savings_contribution,
    "Debt": debt_contribution,
    "Emergency Fund": emergency_contribution
}

most_important_factor = max(
    contributions,
    key=contributions.get
)

print(
    "\nMost Important Factor:",
    most_important_factor
)

print(
    "\nExplainable AI analysis completed successfully!"
)