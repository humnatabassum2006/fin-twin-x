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

# Count users in each risk category
risk_summary = df["risk_category"].value_counts()

# Total users
total_users = len(df)

# Calculate percentages
high_risk = risk_summary.get("High Risk", 0)
medium_risk = risk_summary.get("Medium Risk", 0)
low_risk = risk_summary.get("Low Risk", 0)

high_risk_percentage = (high_risk / total_users) * 100
medium_risk_percentage = (medium_risk / total_users) * 100
low_risk_percentage = (low_risk / total_users) * 100

# Display Risk Summary
print("===== Financial Risk Summary =====")

print("Total Users:", total_users)

print("\nHigh Risk Users:", high_risk)
print("High Risk Percentage:", round(high_risk_percentage, 2), "%")

print("\nMedium Risk Users:", medium_risk)
print("Medium Risk Percentage:", round(medium_risk_percentage, 2), "%")

print("\nLow Risk Users:", low_risk)
print("Low Risk Percentage:", round(low_risk_percentage, 2), "%")