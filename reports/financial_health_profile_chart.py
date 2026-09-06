import pandas as pd
import matplotlib.pyplot as plt

# Load Financial DNA profiles
df = pd.read_csv("data/financial_dna_profiles.csv")

# Count health profiles
health_summary = df["health_profile"].value_counts()

# Create chart
plt.figure(figsize=(8, 6))

health_summary.plot(kind="bar")

plt.title("Financial Health Profile Distribution")
plt.xlabel("Financial Health Profile")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    "reports/financial_health_profile_distribution.png"
)

print("Financial health profile chart created successfully!")
print("Chart saved in reports folder.")