import numpy as np
import matplotlib.pyplot as plt

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Same random results every time
np.random.seed(42)

# Generate possible income changes
income_changes = np.random.normal(
    loc=0,
    scale=0.10,
    size=simulations
)

# Simulated future incomes
simulated_income = (
    monthly_income * (1 + income_changes)
)

# Calculate simulated savings
simulated_savings = (
    simulated_income - monthly_expenses
)

# Savings cannot be negative
simulated_savings = np.maximum(
    simulated_savings,
    0
)

# Create histogram
plt.figure(figsize=(10, 6))

plt.hist(
    simulated_savings,
    bins=30
)

plt.title("Monte Carlo Simulation - Possible Monthly Savings")
plt.xlabel("Simulated Monthly Savings")
plt.ylabel("Number of Simulations")

# Save chart
plt.savefig(
    "reports/monte_carlo_savings_distribution.png"
)

print("Monte Carlo chart created successfully!")
print("Chart saved in reports folder.")