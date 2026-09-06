import numpy as np

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Reproducible results
np.random.seed(42)

# Simulate possible future income
simulated_income = np.random.normal(
    monthly_income,
    monthly_income * 0.10,
    simulations
)

# Calculate possible future savings
simulated_savings = (
    simulated_income - monthly_expenses
)

# Savings cannot be negative
simulated_savings = np.maximum(
    simulated_savings,
    0
)

# Calculate savings loss compared with normal savings
normal_savings = monthly_income - monthly_expenses

savings_loss = (
    normal_savings - simulated_savings
)

# 95% Value at Risk
var_95 = np.percentile(
    savings_loss,
    95
)

# 99% Value at Risk
var_99 = np.percentile(
    savings_loss,
    99
)

# Display results
print("===== VALUE AT RISK ANALYSIS =====")

print(
    "Normal Monthly Savings:",
    normal_savings
)

print(
    "95% VaR:",
    round(var_95, 2)
)

print(
    "99% VaR:",
    round(var_99, 2)
)