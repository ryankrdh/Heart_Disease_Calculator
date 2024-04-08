def calculate_probability(user_responses):
    risk_score = 0
    factors = []

    if int(user_responses['Age']) > 50:
        risk_score += 3
        factors.append("Age > 50 years: +3 points")

    gender_points = {'Male': 2, 'Female': 1}
    risk_score += gender_points.get(user_responses['Gender'], 0)
    factors.append(f"{user_responses['Gender']} Gender: +{gender_points.get(user_responses['Gender'], 0)} points")

    family_history_points = {'yes': 3, 'no': 0, 'unknown': 0}
    risk_score += family_history_points.get(user_responses['Family History'], 0)
    factors.append(f"Family History of Heart Disease: +{family_history_points.get(user_responses['Family History'], 0)} points")

    smoking_points = {'yes': 3, 'no': 0, 'occasionally': 1}
    risk_score += smoking_points.get(user_responses['Smoking'], 0)
    factors.append(f"Smoking {user_responses['Smoking']}: +{smoking_points.get(user_responses['Smoking'], 0)} points")

    diet_points = {'healthy': 0, 'unhealthy': 3, 'moderate': 1}
    risk_score += diet_points.get(user_responses['Diet'], 0)
    factors.append(f"Diet {user_responses['Diet']}: +{diet_points.get(user_responses['Diet'], 0)} points")

    activity_points = {'active': 0, 'sedentary': 3, 'moderately active': 1}
    risk_score += activity_points.get(user_responses['Physical Activity'], 0)
    factors.append(f"Physical Activity {user_responses['Physical Activity']}: +{activity_points.get(user_responses['Physical Activity'], 0)} points")

    obesity_points = {'yes': 3, 'no': 0, 'borderline': 1}
    risk_score += obesity_points.get(user_responses['Obesity'], 0)
    factors.append(f"Obesity: +{obesity_points.get(user_responses['Obesity'], 0)} points")

    diabetes_points = {'yes': 3, 'no': 0, 'pre-diabetes': 1}
    risk_score += diabetes_points.get(user_responses['Diabetes'], 0)
    factors.append(f"Diabetes: +{diabetes_points.get(user_responses['Diabetes'], 0)} points")

    bp_points = {'yes': 3, 'no': 0, 'borderline': 1}
    risk_score += bp_points.get(user_responses['High Blood Pressure'], 0)
    factors.append(f"High Blood Pressure: +{bp_points.get(user_responses['High Blood Pressure'], 0)} points")

    mental_health_points = {'yes': 3, 'no': 0, 'sometimes': 1}
    risk_score += mental_health_points.get(user_responses['Stress and Mental Health'], 0)
    factors.append(f"Stress and Mental Health Issues: +{mental_health_points.get(user_responses['Stress and Mental Health'], 0)} points")

    alcohol_points = {'none': 0, 'light': 1, 'moderate': 2, 'heavy': 3}
    risk_score += alcohol_points.get(user_responses['Alcohol Consumption'], 0)
    factors.append(f"Alcohol Consumption {user_responses['Alcohol Consumption']}: +{alcohol_points.get(user_responses['Alcohol Consumption'], 0)} points")

    sleep_points = {'regular': 0, 'irregular': 2, 'often disturbed': 1}
    risk_score += sleep_points.get(user_responses['Sleep Patterns'], 0)
    factors.append(f"Sleep Patterns {user_responses['Sleep Patterns']}: +{sleep_points.get(user_responses['Sleep Patterns'], 0)} points")

    probability = min(risk_score * 2, 100)  # Adjusted calculation method

    risk_category = "High risk of heart disease." if risk_score > 20 else "Moderate risk of heart disease." if risk_score > 10 else "Low risk of heart disease."
    equation = f"Risk Score: {risk_score} * 2% per Point = {probability}% Chance"
    
    return risk_category, factors, equation, probability
