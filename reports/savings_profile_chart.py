import pandas as pd
import matplotlib.pyplot as plt

# Load Financial DNA profiles
df = pd.read_csv("data/financial_dna_profiles.csv")

# Count savings profiles
savings_summary = df["savings_profile"].value_counts()

# Create chart
plt.figure(figsize=(8, 6))

savings_summary.plot(kind="bar")

plt.title("Savings Profile Distribution")
plt.xlabel("Savings Profile")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    "reports/savings_profile_distribution.png"
)

print("Savings profile chart created successfully!")
print("Chart saved in reports folder.")