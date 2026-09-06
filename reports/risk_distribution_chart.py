import pandas as pd
import matplotlib.pyplot as plt

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

# Create Risk Distribution Chart
plt.figure(figsize=(8, 6))

risk_summary.plot(kind="bar")

plt.title("Financial Risk Distribution")
plt.xlabel("Risk Category")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig("reports/risk_distribution.png")