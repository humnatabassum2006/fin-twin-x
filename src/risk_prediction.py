# Financial Health Score
health_score = 55.79

# Classify risk
if health_score >= 70:
    risk_category = "Low Risk"
elif health_score >= 40:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

print("===== Risk Prediction =====")
print("Financial Health Score:", health_score)
print("Risk Category:", risk_category)