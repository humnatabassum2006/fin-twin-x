import pandas as pd

# Load Financial DNA profiles
df = pd.read_csv("data/financial_dna_profiles.csv")

print("===== FINANCIAL DNA SUMMARY =====")

print("\nTotal Users:", len(df))

# Savings Profile Summary
print("\n===== SAVINGS PROFILES =====")
print(df["savings_profile"].value_counts())

# Debt Profile Summary
print("\n===== DEBT PROFILES =====")
print(df["debt_profile"].value_counts())

# Emergency Fund Summary
print("\n===== EMERGENCY FUND PROFILES =====")
print(df["emergency_fund_profile"].value_counts())

# Overall Health Summary
print("\n===== OVERALL HEALTH PROFILES =====")
print(df["health_profile"].value_counts())

# Average Financial Health Score
average_health = df["financial_health_score"].mean()

print(
    "\nAverage Financial Health Score:",
    round(average_health, 2)
)