from flask import Flask, render_template, request
import probability  # Assume risk_factors are calculated and stored in a Python file named probability.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data directly
    data = {
        "age": request.form.get('age'),
        "sex": request.form.get('sex'),
        "cp": request.form.get('cp'),
        "trestbps": request.form.get('trestbps'),
        "chol": request.form.get('chol'),
        "fbs": request.form.get('fbs'),
        "restecg": request.form.get('restecg'),
        "thalach": request.form.get('thalach'),
        "exang": request.form.get('exang'),
        "oldpeak": request.form.get('oldpeak'),
        "slope": request.form.get('slope'),
        "ca": request.form.get('ca'),
        "thal": request.form.get('thal')
    }

    total_risk_factors = []
    product_of_risks = 1.0

    for key, value in data.items():
        risk_value = probability.risk_factors[key].get(value, 1)  # Default to 1 if no risk factor is found
        total_risk_factors.append((key, value, risk_value))
        product_of_risks *= risk_value

    # Calculate the chance of getting heart disease
    product_of_risks = 1 - product_of_risks
    result_message = f"Chance of getting heart disease is: {product_of_risks:.2%}"

    return render_template('result.html', total_risk_factors=total_risk_factors, result_message=result_message)

if __name__ == "__main__":
    app.run(debug=True)
