import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load financial data
df = pd.read_csv("data/financial_dna.csv")

# Features for anomaly detection
features = [
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "savings_rate",
    "debt_to_income",
    "emergency_fund_months"
]

# Create Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Detect anomalies
df["anomaly"] = model.fit_predict(df[features])

# Convert labels
df["anomaly_status"] = df["anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Count normal and anomalous users
anomaly_summary = df["anomaly_status"].value_counts()

# Create chart
plt.figure(figsize=(8, 6))

anomaly_summary.plot(kind="bar")

plt.title("Financial Anomaly Detection")
plt.xlabel("User Status")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    "reports/anomaly_distribution.png"
)

print("Anomaly chart created successfully!")
print("Chart saved in reports folder.")