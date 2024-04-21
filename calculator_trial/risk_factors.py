import pandas as pd

def get_risk_percentages():
    data = pd.read_csv('heart.csv')
    data['age'] = data['age'].apply(categorize_age)
    data['trestbps'] = data['trestbps'].apply(categorize_trestbps)
    data['chol'] = data['chol'].apply(categorize_chol)
    data['thalach'] = data['thalach'].apply(categorize_thalach)
    data['oldpeak'] = data['oldpeak'].apply(categorize_oldpeak)
    return calculate_option_risk(data)

def categorize_age(age):
    if age < 40:
        return '2'
    elif age < 60:
        return '1'
    else:
        return '0'

def categorize_trestbps(trestbps):
    trestbps = int(trestbps)
    if trestbps < 100:
        return '3'
    elif trestbps < 110:
        return '2'
    elif trestbps < 120:
        return '1'
    else:
        return '0'

def categorize_chol(chol):
    chol = int(chol)
    if chol < 200:
        return '2'
    elif chol < 240:
        return '1'
    else:
        return '0'

def categorize_thalach(thalach):
    thalach = int(thalach)
    if thalach > 140:
        return '3'
    elif thalach > 120:
        return '2'
    elif thalach > 100:
        return '1'
    else:
        return '0'

def categorize_oldpeak(oldpeak):
    oldpeak = float(oldpeak)
    if oldpeak < 1:
        return '3'
    elif oldpeak < 2:
        return '2'
    elif oldpeak < 3:
        return '1'
    else:
        return '0'

def calculate_option_risk(data):
    descriptive_labels = {
        'age': ['Under 40', '40-59', '60+'],
        'sex': ['Male', 'Female'],
        'cp': ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'],
        'trestbps': ['Under 100', '100-109', '110-119', '120+'],
        'chol': ['Under 200', '200-239', '240+'],
        'fbs': ['Yes', 'No'],
        'restecg': ['Left ventricular hypertrophy', 'ST-T wave abnormality', 'Normal'],
        'thalach': ['Above 140', '121-140', '100-120', 'Less than 100'],
        'exang': ['Yes', 'No'],
        'oldpeak': ['Less than 1 mm', '1-2 mm', '2-3 mm', 'More than 3 mm'],
        'slope': ['Upsloping', 'Flat', 'Downsloping'],
        'ca': ['3 Major Vessels', '2 Major Vessels', '1 Major Vessels', '0 Major Vessels'],
        'thal': ['Normal', 'Fixed defect', 'Reversible defect']
    }

    risk_summary = {}
    for factor, labels in descriptive_labels.items():
        data[factor] = data[factor].astype(str)  # Ensure data type consistency
        mapped_risks = {label: 0.0 for label in labels}  # Initialize risk for all labels

        if factor in data:
            count_with_disease = data[data['target'] == 1][factor].value_counts().sort_index()
            total_counts = data[factor].value_counts().sort_index()
            risk_percentage = (count_with_disease / total_counts * 100).fillna(0)
            
            for key, value in risk_percentage.items():
                if int(float(key)) < len(labels):
                    mapped_risks[labels[int(float(key))]] = value

        risk_summary[factor] = mapped_risks

    return risk_summary

if __name__ == "__main__":
    risk_percentages = get_risk_percentages()
    for factor, risks in risk_percentages.items():
        print(f"\nRisk Factor: {factor.upper()}")
        for description, percentage in risks.items():
            print(f"  {description}: {percentage:.2f}% risk of heart disease")



# import pandas as pd

# # Load the data
# data = pd.read_csv('heart.csv')

# # Helper function to categorize age
# def categorize_age(age):
#     if age < 40:
#         return '2'  # 'Under 40'
#     elif age < 60:
#         return '1'  # '40-59'
#     else:
#         return '0'  # '60+'

# # Categorize age in the dataset
# data['age'] = data['age'].apply(categorize_age)

# # Helper function to categorize resting blood pressure (trestbps)
# def categorize_trestbps(trestbps):
#     trestbps = int(trestbps)  # Convert to integer if it's not already
#     if trestbps < 100:
#         return '3'  # 'Under 100'
#     elif trestbps < 110:
#         return '2'  # '100-109'
#     elif trestbps < 120:
#         return '1'  # '110-119'
#     else:
#         return '0'  # '120+'

# # Apply categorization to trestbps in the dataset
# data['trestbps'] = data['trestbps'].apply(categorize_trestbps)

# # Helper function to categorize cholesterol (chol)
# def categorize_chol(chol):
#     chol = int(chol)  # Convert to integer if it's not already
#     if chol < 200:
#         return '2'  # 'Under 200'
#     elif chol < 240:
#         return '1'  # '200-239'
#     else:
#         return '0'  # '240+'

# # Apply categorization to chol in the dataset
# data['chol'] = data['chol'].apply(categorize_chol)


# # Helper function to categorize maximum heart rate achieved (thalach)
# def categorize_thalach(thalach):
#     thalach = int(thalach)  # Ensure the value is treated as an integer
#     if thalach > 140:
#         return '3'  # 'Above 140'
#     elif thalach > 120:
#         return '2'  # '121-140'
#     elif thalach > 100:
#         return '1'  # '100-120'
#     else:
#         return '0'  # 'Less than 100'

# # Apply the categorization to thalach in the dataset
# data['thalach'] = data['thalach'].apply(categorize_thalach)

# # Helper function to categorize ST depression induced by exercise relative to rest (oldpeak)
# def categorize_oldpeak(oldpeak):
#     oldpeak = float(oldpeak)  # Ensure the value is treated as a float
#     if oldpeak < 1:
#         return '3'  # 'Less than 1 mm'
#     elif oldpeak < 2:
#         return '2'  # '1-2 mm'
#     elif oldpeak < 3:
#         return '1'  # '2-3 mm'
#     else:
#         return '0'  # 'More than 3 mm'

# # Apply the categorization to oldpeak in the dataset
# data['oldpeak'] = data['oldpeak'].apply(categorize_oldpeak)

# # With oldpeak now properly categorized, you can calculate the risk percentages

# def calculate_option_risk(data):
#     descriptive_labels = {
#         'age': ['Under 40', '40-59', '60+'],
#         'sex': ['Male', 'Female'],
#         'cp': ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'],
#         'trestbps': ['Under 100', '100-109', '110-119', '120+'],
#         'chol': ['Under 200', '200-239', '240+'],
#         'fbs': ['Yes', 'No'],
#         'restecg': ['Left ventricular hypertrophy', 'ST-T wave abnormality', 'Normal'],
#         'thalach': ['Above 140', '121-140', '100-120', 'Less than 100'],
#         'exang': ['Yes', 'No'],
#         'oldpeak': ['Less than 1 mm', '1-2 mm', '2-3 mm', 'More than 3 mm'],
#         'slope': ['Upsloping', 'Flat', 'Downsloping'],
#         'ca': ['3 Major Vessels', '2 Major Vessels', '1 Major Vessels', '0 Major Vessels'],
#         'thal': ['Normal', 'Fixed defect', 'Reversible defect']
#     }

#     risk_summary = {}
#     for factor, labels in descriptive_labels.items():
#         data[factor] = data[factor].astype(str)  # Ensure data type consistency
#         mapped_risks = {label: 0.0 for label in labels}  # Initialize risk for all labels

#         if factor in data:
#             count_with_disease = data[data['target'] == 1][factor].value_counts().sort_index()
#             total_counts = data[factor].value_counts().sort_index()
#             risk_percentage = (count_with_disease / total_counts * 100).fillna(0)
            
#             for key, value in risk_percentage.items():
#                 if int(float(key)) < len(labels):
#                     mapped_risks[labels[int(float(key))]] = value

#         risk_summary[factor] = mapped_risks

#     return risk_summary

# risk_percentages = calculate_option_risk(data)

# # Print detailed descriptive output for each risk factor
# for factor, risks in risk_percentages.items():
#     print(f"\nRisk Factor: {factor.upper()}")
#     for description, percentage in risks.items():
#         print(f"  {description}: {percentage:.2f}% risk of heart disease")
