
import json
from risk_factors import get_risk_percentages

# Get the risk percentages calculated in risk_factors.py
risk_percentages = get_risk_percentages()

# Convert risk percentages to decimal format
risk_factors = {factor: {description: percentage / 100 for description, percentage in risks.items()}
                for factor, risks in risk_percentages.items()}

# Export the risk_factors to a JSON file
with open('risk_factors.json', 'w') as file:
    json.dump(risk_factors, file, indent=4)

# Print detailed descriptive output for each risk factor with decimal values
print("Detailed Risk Factors in Decimal Format:")
for factor, risks in risk_factors.items():
    print(f"\nRisk Factor: {factor.upper()}")
    for description, decimal in risks.items():
        # Print the decimal risk percentage without the '%' sign and format as a decimal
        print(f"  {description}: {decimal:.3f} risk of heart disease")








# from risk_factors import get_risk_percentages

# # Get the risk percentages calculated in risk_factors.py
# risk_percentages = get_risk_percentages()

# # Convert risk percentages to decimal format
# risk_factors = {}
# for factor, risks in risk_percentages.items():
#     # Initialize a dictionary for each factor
#     risk_factors[factor] = {}
#     for description, percentage in risks.items():
#         # Convert percentage to decimal and store it
#         risk_factors[factor][description] = percentage / 100.0







# import pandas as pd

# # Load data
# data = pd.read_csv('heart.csv')

# # Function to calculate the probability of heart disease given a risk factor
# def calculate_probability(data, factor):
#     count_with_disease = data[data['target'] == 1][factor].value_counts().sort_index()
#     total_counts = data[factor].value_counts().sort_index()
#     probabilities = (count_with_disease / total_counts * 100).fillna(0)
#     return probabilities


# # List of risk factors
# risk_factors = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# # Calculate and categorize probabilities for each risk factor
# risk_categorizations = {}
# for factor in risk_factors:
#     probabilities = calculate_probability(data, factor)
#     categorized_risks = probabilities.apply(categorize_risk)
#     risk_categorizations[factor] = categorized_risks.to_dict()  # Convert to dictionary for easier lookup

# # Function to calculate cumulative risk score based on user responses
# def get_risk_score(user_responses):
#     risk_score = 0
#     points = {'Very High': 3, 'High': 2, 'Moderate': 1, 'Low': 0}

#     # Compute the score based on the risk level of each factor
#     for factor, value in user_responses.items():
#         risk_level = risk_categorizations[factor].get(value, 'Low')  # Default to 'Low' if no key is found
#         risk_score += points[risk_level]

#     return risk_score



