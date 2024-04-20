def calculate_probability(user_responses):
    risk_score = 0
    factors = []

    # Age
    age = int(user_responses['age'])
    if age < 40:
        risk_score += 0
    elif 40 <= age < 60:
        risk_score += 1
    elif 60 <= age < 80:
        risk_score += 2
    else:
        risk_score += 3
    factors.append(f"Age: {age}, Points: {risk_score}")

    # Sex
    sex_points = {'male': 1, 'female': 0}
    risk_score += sex_points[user_responses['sex'].lower()]
    factors.append(f"Sex ({user_responses['sex']}): +{sex_points[user_responses['sex'].lower()]} points")

    # Chest Pain Type (cp)
    cp_points = {'0': 0, '1': 1, '2': 2, '3': 3}
    risk_score += cp_points[user_responses['cp']]
    factors.append(f"Chest Pain Type {user_responses['cp']}: +{cp_points[user_responses['cp']]} points")

    # Resting Blood Pressure (trestbps)
    trestbps = int(user_responses['trestbps'])
    if trestbps < 100:
        risk_score += 0
    elif 100 <= trestbps < 110:
        risk_score += 1
    elif 110 <= trestbps < 120:
        risk_score += 2
    else:
        risk_score += 3
    factors.append(f"Resting Blood Pressure {trestbps} mm Hg: +{risk_score} points")

    # Cholesterol (chol)
    chol = int(user_responses['chol'])
    if chol < 200:
        risk_score += 0
    elif 200 <= chol < 240:
        risk_score += 1
    else:
        risk_score += 2
    factors.append(f"Cholesterol {chol} mg/dL: +{risk_score} points")

    # Fasting Blood Sugar (fbs)
    fbs_points = {'0': 0, '1': 1}
    risk_score += fbs_points[user_responses['fbs']]
    factors.append(f"Fasting Blood Sugar ({user_responses['fbs'] == '1' and '>120 mg/dL' or '<120 mg/dL'}): +{fbs_points[user_responses['fbs']]} points")

    # Resting Electrocardiographic Results (restecg)
    restecg_points = {'0': 0, '1': 1, '2': 2}
    risk_score += restecg_points[user_responses['restecg']]
    factors.append(f"Resting ECG {user_responses['restecg']}: +{restecg_points[user_responses['restecg']]} points")

    # Maximum Heart Rate Achieved (thalach)
    thalach = int(user_responses['thalach'])
    if thalach > 140:
        risk_score += 0
    elif 121 <= thalach <= 140:
        risk_score += 1
    elif 100 <= thalach < 121:
        risk_score += 2
    else:
        risk_score += 3
    factors.append(f"Maximum Heart Rate {thalach} bpm: +{risk_score} points")

    # Exercise Induced Angina (exang)
    exang_points = {'0': 0, '1': 1}
    risk_score += exang_points[user_responses['exang']]
    factors.append(f"Exercise Induced Angina ({user_responses['exang'] == '1' and 'Yes' or 'No'}): +{exang_points[user_responses['exang']]} points")

    # ST Depression (oldpeak)
    oldpeak = float(user_responses['oldpeak'])
    if oldpeak < 1:
        risk_score += 0
    elif 1 <= oldpeak < 2:
        risk_score += 1
    elif 2 <= oldpeak < 3:
        risk_score += 2
    else:
        risk_score += 3
    factors.append(f"ST Depression {oldpeak} mm: +{risk_score} points")

    # Slope of the Peak Exercise ST Segment (slope)
    slope_points = {'0': 0, '1': 1, '2': 2}
    risk_score += slope_points[user_responses['slope']]
    factors.append(f"Slope of Peak Exercise ST Segment {user_responses['slope']}: +{slope_points[user_responses['slope']]} points")

    # Number of Major Vessels Colored by Fluoroscopy (ca)
    ca_points = {'0': 0, '1': 1, '2': 2, '3': 3}
    risk_score += ca_points[user_responses['ca']]
    factors.append(f"Number of Major Vessels {user_responses['ca']}: +{ca_points[user_responses['ca']]} points")

    # Thalassemia (thal)
    thal_points = {'3': 0, '1': 1, '6': 2}
    risk_score += thal_points[user_responses['thal']]
    factors.append(f"Thalassemia {user_responses['thal']}: +{thal_points[user_responses['thal']]} points")

    # Calculate total probability
    probability = min(risk_score * 2, 100)  # Adjusted calculation method
    risk_category = "High risk of heart disease." if risk_score > 20 else "Moderate risk of heart disease." if risk_score > 10 else "Low risk of heart disease."
    equation = f"Risk Score: {risk_score} * 2% per Point = {probability}% Chance"

    return risk_category, factors, equation, probability



# def calculate_probability(user_responses):
#     risk_score = 0
#     factors = []

#     if int(user_responses['Age']) > 50:
#         risk_score += 3
#         factors.append("Age > 50 years: +3 points")

#     gender_points = {'Male': 2, 'Female': 1}
#     risk_score += gender_points.get(user_responses['Gender'], 0)
#     factors.append(f"{user_responses['Gender']} Gender: +{gender_points.get(user_responses['Gender'], 0)} points")

#     family_history_points = {'yes': 3, 'no': 0, 'unknown': 0}
#     risk_score += family_history_points.get(user_responses['Family History'], 0)
#     factors.append(f"Family History of Heart Disease: +{family_history_points.get(user_responses['Family History'], 0)} points")

#     smoking_points = {'yes': 3, 'no': 0, 'occasionally': 1}
#     risk_score += smoking_points.get(user_responses['Smoking'], 0)
#     factors.append(f"Smoking {user_responses['Smoking']}: +{smoking_points.get(user_responses['Smoking'], 0)} points")

#     diet_points = {'healthy': 0, 'unhealthy': 3, 'moderate': 1}
#     risk_score += diet_points.get(user_responses['Diet'], 0)
#     factors.append(f"Diet {user_responses['Diet']}: +{diet_points.get(user_responses['Diet'], 0)} points")

#     activity_points = {'active': 0, 'sedentary': 3, 'moderately active': 1}
#     risk_score += activity_points.get(user_responses['Physical Activity'], 0)
#     factors.append(f"Physical Activity {user_responses['Physical Activity']}: +{activity_points.get(user_responses['Physical Activity'], 0)} points")

#     obesity_points = {'yes': 3, 'no': 0, 'borderline': 1}
#     risk_score += obesity_points.get(user_responses['Obesity'], 0)
#     factors.append(f"Obesity: +{obesity_points.get(user_responses['Obesity'], 0)} points")

#     diabetes_points = {'yes': 3, 'no': 0, 'pre-diabetes': 1}
#     risk_score += diabetes_points.get(user_responses['Diabetes'], 0)
#     factors.append(f"Diabetes: +{diabetes_points.get(user_responses['Diabetes'], 0)} points")

#     bp_points = {'yes': 3, 'no': 0, 'borderline': 1}
#     risk_score += bp_points.get(user_responses['High Blood Pressure'], 0)
#     factors.append(f"High Blood Pressure: +{bp_points.get(user_responses['High Blood Pressure'], 0)} points")

#     mental_health_points = {'yes': 3, 'no': 0, 'sometimes': 1}
#     risk_score += mental_health_points.get(user_responses['Stress and Mental Health'], 0)
#     factors.append(f"Stress and Mental Health Issues: +{mental_health_points.get(user_responses['Stress and Mental Health'], 0)} points")

#     alcohol_points = {'none': 0, 'light': 1, 'moderate': 2, 'heavy': 3}
#     risk_score += alcohol_points.get(user_responses['Alcohol Consumption'], 0)
#     factors.append(f"Alcohol Consumption {user_responses['Alcohol Consumption']}: +{alcohol_points.get(user_responses['Alcohol Consumption'], 0)} points")

#     sleep_points = {'regular': 0, 'irregular': 2, 'often disturbed': 1}
#     risk_score += sleep_points.get(user_responses['Sleep Patterns'], 0)
#     factors.append(f"Sleep Patterns {user_responses['Sleep Patterns']}: +{sleep_points.get(user_responses['Sleep Patterns'], 0)} points")

#     probability = min(risk_score * 2, 100)  # Adjusted calculation method

#     risk_category = "High risk of heart disease." if risk_score > 20 else "Moderate risk of heart disease." if risk_score > 10 else "Low risk of heart disease."
#     equation = f"Risk Score: {risk_score} * 2% per Point = {probability}% Chance"
    
#     return risk_category, factors, equation, probability
