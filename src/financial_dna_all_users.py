import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")


# -----------------------------
# Savings Profile
# -----------------------------

def classify_savings(rate):

    if rate >= 30:
        return "Strong Saver"
    elif rate >= 20:
        return "Moderate Saver"
    else:
        return "Low Saver"


df["savings_profile"] = df["savings_rate"].apply(
    classify_savings
)


# -----------------------------
# Debt Profile
# -----------------------------

def classify_debt(ratio):

    if ratio <= 20:
        return "Low Debt"
    elif ratio <= 40:
        return "Moderate Debt"
    else:
        return "High Debt"


df["debt_profile"] = df["debt_to_income"].apply(
    classify_debt
)


# -----------------------------
# Emergency Fund Profile
# -----------------------------

def classify_emergency_fund(months):

    if months >= 6:
        return "Excellent Emergency Fund"
    elif months >= 3:
        return "Good Emergency Fund"
    else:
        return "Weak Emergency Fund"


df["emergency_fund_profile"] = df[
    "emergency_fund_months"
].apply(classify_emergency_fund)


# -----------------------------
# Overall Health Profile
# -----------------------------

def classify_health(score):

    if score >= 70:
        return "Healthy"
    elif score >= 40:
        return "Moderate"
    else:
        return "Financially Stressed"


df["health_profile"] = df[
    "financial_health_score"
].apply(classify_health)


# -----------------------------
# Save All Financial DNA Profiles
# -----------------------------

df.to_csv(
    "data/financial_dna_profiles.csv",
    index=False
)


# -----------------------------
# Display Results
# -----------------------------

print("===== FINANCIAL DNA PROFILES =====")

print("Total Users:", len(df))

print("\nSavings Profiles:")
print(df["savings_profile"].value_counts())

print("\nDebt Profiles:")
print(df["debt_profile"].value_counts())

print("\nEmergency Fund Profiles:")
print(df["emergency_fund_profile"].value_counts())

print("\nHealth Profiles:")
print(df["health_profile"].value_counts())

print(
    "\nFinancial DNA Profiles saved successfully!"
)