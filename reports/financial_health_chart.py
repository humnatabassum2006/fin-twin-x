import pandas as pd
import matplotlib.pyplot as plt

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Create Financial Health Score distribution chart
plt.figure(figsize=(10, 6))

plt.hist(df["financial_health_score"], bins=20)

plt.title("Financial Health Score Distribution")
plt.xlabel("Financial Health Score")
plt.ylabel("Number of Users")

plt.savefig("reports/financial_health_distribution.png")