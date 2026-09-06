import pandas as pd
import matplotlib.pyplot as plt

# Load Financial DNA profiles
df = pd.read_csv("data/financial_dna_profiles.csv")

# Count debt profiles
debt_summary = df["debt_profile"].value_counts()

# Create chart
plt.figure(figsize=(8, 6))

debt_summary.plot(kind="bar")

plt.title("Debt Profile Distribution")
plt.xlabel("Debt Profile")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    "reports/debt_profile_distribution.png"
)

print("Debt profile chart created successfully!")
print("Chart saved in reports folder.")