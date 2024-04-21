import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Load the dataset
heart_data = pd.read_csv('heart.csv')

# Separate features and target variable
X = heart_data.drop('output', axis=1)
y = heart_data['output']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create and train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Evaluate the model's performance
# accuracy = nb_model.score(X_test, y_test)
# print(f"Accuracy: {accuracy * 100:.2f}%")

def predict_heart_attack():
    """
    Function to get user input and predict the probability of a heart attack.
    Returns:
    - Rendered HTML template with the predicted probability of a heart attack.
    """
    features = []
    input_fields = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
    try:
        for field in input_fields:
            value = request.form[field]
            if field == 'oldpeak':  # 'oldpeak' needs to be converted to float
                features.append(float(value))
            else:  # Other fields are integers
                features.append(int(value))
    except ValueError as e:
        print("Invalid input:", e)
        return "Invalid input. Please enter valid numeric values."

    # Predicting the probability using the trained model
    features_scaled = [features]  # Wrap in a list to match input shape
    probability = nb_model.predict_proba(features_scaled)[0]
    probability_heart_attack = f"{probability[1] * 100:.2f}%"
    return render_template('index.html', probability=probability_heart_attack)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index.html template and handles the form submission.

    Returns:
    - render_template (function): Renders the index.html template.
    - predict_heart_attack (function): Calls the predict_heart_attack function to predict the probability of a heart attack.
    """
    if request.method == 'POST':
        return predict_heart_attack()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)