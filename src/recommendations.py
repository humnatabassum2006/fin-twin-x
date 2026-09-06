# User's financial information
financial_health_score = 55.79
savings_rate = 40
debt_to_income = 33.33
emergency_fund_months = 0.67

print("===== FINANCIAL RECOMMENDATIONS =====")

# Financial Health recommendation
if financial_health_score < 40:
    print("🔴 Focus on improving your overall financial health.")
elif financial_health_score < 70:
    print("🟡 Your financial health is moderate. Focus on improving savings and reducing debt.")
else:
    print("🟢 Your financial health is strong. Continue maintaining good financial habits.")

# Savings recommendation
if savings_rate < 20:
    print("💰 Increase your savings rate. Try to save at least 20% of your income.")
else:
    print("💰 Your savings rate is reasonable. Keep building your savings.")

# Debt recommendation
if debt_to_income > 40:
    print("📉 Your debt-to-income ratio is high. Focus on reducing your debt.")
else:
    print("📉 Your debt-to-income ratio is within a reasonable range.")

# Emergency fund recommendation
if emergency_fund_months < 3:
    print("🛡️ Build an emergency fund covering at least 3 months of expenses.")
else:
    print("🛡️ Your emergency fund provides a good level of protection.")