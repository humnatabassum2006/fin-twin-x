import pandas as pd
import matplotlib.pyplot as plt

# Load Financial DNA profiles
df = pd.read_csv("data/financial_dna_profiles.csv")

# Count emergency fund profiles
emergency_summary = df["emergency_fund_profile"].value_counts()

# Create chart
plt.figure(figsize=(8, 6))

emergency_summary.plot(kind="bar")

plt.title("Emergency Fund Profile Distribution")
plt.xlabel("Emergency Fund Profile")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    "reports/emergency_fund_profile_distribution.png"
)

print("Emergency fund profile chart created successfully!")
print("Chart saved in reports folder.")