from flask import Flask, render_template, request
from probability import calculate_probability

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    user_responses = {
        "Age": request.form['age'],
        "Gender": request.form['gender'],
        "Family History": request.form['familyHistory'],
        "Smoking": request.form['smoking'],
        "Diet": request.form['diet'],
        "Physical Activity": request.form['physicalActivity'],
        "Obesity": request.form['obesity'],
        "Diabetes": request.form['diabetes'],
        "High Blood Pressure": request.form['highBloodPressure'],
        "Stress and Mental Health": request.form['stressAndMentalHealth'],
        "Alcohol Consumption": request.form['alcoholConsumption'],
        "Sleep Patterns": request.form['sleepPatterns']
    }
    result_message, factors, equation, probability = calculate_probability(user_responses)
    return render_template('result.html', result_message=result_message, factors=factors, equation=equation, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)