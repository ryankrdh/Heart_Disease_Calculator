# Heart Disease Calculator

### CS5002 Discrete Structure Final Project

## How to get started

### Click ⬇ to START!<br><br>
<a href="https://rhk4783.pythonanywhere.com/"><img src="heart_icon.ico" width="100" height="100"></a>

### or

## Run in Visual Studio Code

### Step 1: Create your virtual environment
    python3 -m venv venv


### Step 2: Start your virtual environment
    source venv/bin/activate

### Step 3: Install dependencies

(May need to upgrade pip)
    
    pip3 install --upgrade pip

    pip3 install -r requirements.txt

### Step 4: Run the app
    python3 app.py

## Introduction

Our application is a heart disease risk analysis tool designed to calculate the probability of an individual’s risk of developing heart disease. Utilizing advanced statistical methods and discrete mathematics principles, this tool analyzes a wide range of factors to quantify risk levels accurately. Our goal is to provide a resource that individuals and healthcare providers can use to assess heart disease risk and implement preventive measures effectively.

## Data Dictionary

The application evaluates the following factors to predict heart disease risk:

# Heart Disease Risk Factors

## Age (age)
Description: Age in years of the patient.  
Role in Risk Assessment: Older age is generally associated with a higher risk of heart disease.

### Values and Scoring
- **Under 40**:
  - **Risk**: Significantly lower
  - **Value Points**: 0
  - **Explanation**: Lower risk due to younger age.
- **Age 40-59**:
  - **Risk**: Approximately 40%
  - **Value Points**: 1
  - **Explanation**: Moderate risk reflecting increased age.
- **Age 60-79**:
  - **Risk**: Approximately 75%
  - **Value Points**: 2
  - **Explanation**: Higher risk as age increases.
- **Age 80 and above**:
  - **Risk**: Approximately 86%
  - **Value Points**: 3
  - **Explanation**: Highest risk category due to advanced age.

## Sex (sex)
Description: Biological sex of the patient.  
Role in Risk Assessment: Sex can influence the risk and presentation of heart disease, with males typically at higher risk.

### Values
- **Female**:
  - **Value Points**: 0
  - **Explanation**: Typically, women have a lower risk of heart disease compared to men until the age of menopause, after which the risk increases but still remains lower than that for men of similar age.
- **Male**:
  - **Value Points**: 1
  - **Explanation**: Men have a higher risk of developing heart disease at an earlier age, which is believed to be partly due to the protective effects of estrogen in women and differences in cholesterol metabolism.

## Chest Pain Type (cp)
**Description:** Type of chest pain experienced by the patient.  
**Role in Risk Assessment:** Certain types of chest pain are more closely associated with heart conditions than others, with asymptomatic pain often being the most severe indicator.

### Values
- **0: Typical angina**:
  - **Explanation**: This type of pain is directly related to heart problems and occurs as a predictable pattern of chest discomfort due to heart strain, usually triggered by physical activity or stress.
- **1: Atypical angina**:
  - **Explanation**: Less directly associated with heart disease but still considered related to cardiovascular issues, presenting as chest pain but not in the typical manner or location.
- **2: Non-anginal pain**:
  - **Explanation**: Pain that is not related to the heart, typically sharper and not associated with physical or emotional stress.
- **3: Asymptomatic**:
  - **Explanation**: The absence of symptoms can sometimes be the most dangerous, as it includes individuals who do not experience chest pain yet may still have significant heart disease.

## Resting Blood Pressure (trestbps)
Description: Blood pressure (in mm Hg) taken while the patient is in a resting state.  
Role in Risk Assessment: High resting blood pressure can indicate stress on the heart or cardiovascular disease.

### Values and Scoring
- **SBP 90-99 mm Hg**:
  - **Risk**: Baseline risk
  - **Value Points**: 0
  - **Explanation**: Lowest observed risk of ASCVD, representing minimal cardiovascular stress.
- **SBP 100-109 mm Hg**:
  - **Risk**: Moderate increase
  - **Value Points**: 1
  - **Explanation**: Moderate risk, with a significant stepwise increase in ASCVD prevalence and coronary artery calcium compared to the baseline.
- **SBP 110-119 mm Hg**:
  - **Risk**: High increase
  - **Value Points**: 2
  - **Explanation**: Higher risk, correlating with an even greater prevalence of risk factors and higher incidence of ASCVD events.
- **SBP 120-129 mm Hg**:
  - **Risk**: Highest increase
  - **Value Points**: 3
  - **Explanation**: This range sees the highest stepwise increase in both coronary artery calcium presence and ASCVD risk, highlighting the critical need for early preventive measures.

### Notes
- The study underscores the importance of maintaining SBP levels within the optimal range to reduce ASCVD risk.
- Every 10-mm Hg increase in SBP is associated with a 53% higher risk for ASCVD, indicating the importance of blood pressure control even within what is traditionally considered a normal range.

## Cholesterol (chol)
Description: Serum cholesterol in mg/dL.
Role in Risk Assessment: High cholesterol levels can lead to blocked arteries, increasing the risk of heart disease.

### Values and Scoring
- **Under 200 mg/dL**:
  - **Risk**: Desirable
  - **Value Points**: 0
  - **Explanation**: Optimal level with the lowest risk for cardiovascular disease. It is considered healthy and indicates lower CHD risks.
- **200-239 mg/dL**:
  - **Risk**: Borderline high
  - **Value Points**: 1
  - **Explanation**: Moderate risk where lifestyle changes and monitoring are recommended to prevent progression to high cholesterol levels.
- **240 mg/dL and above**:
  - **Risk**: High
  - **Value Points**: 2
  - **Explanation**: High risk indicating a significant chance of developing cardiovascular diseases such as CHD. Active treatment including lifestyle changes and possibly medications are usually required.

### Notes
- For every 1-mmol/L increase in total cholesterol, the risk for coronary heart disease (CHD) increases by about 20% in women and 24% in men. This implies that high cholesterol is more potent in elevating heart disease risk in men compared to women.
- Unlike its strong correlation with CHD, high cholesterol has a minimal impact on the risk of total stroke in both sexes.

### Sex Differences
- The effect of high cholesterol on CHD is slightly stronger in men than in women, with women having a 4% lower relative risk compared to men for similar elevations in cholesterol levels.


## Fasting Blood Sugar (fbs)
**Description:** Indicates if fasting blood sugar is above 120 mg/dl.  
**Role in Risk Assessment:** High fasting blood sugar is a marker of diabetes, which is a risk factor for heart disease.

### Values
- **0**: Below 120 mg/dL
  - **Explanation**: Indicates a normal range of blood sugar, suggesting no immediate risk of diabetes.
- **1**: Above 120 mg/dL
  - **Explanation**: Elevated blood sugar levels are a risk factor for diabetes, which itself is a major risk factor for cardiovascular disease, particularly due to the damage high glucose levels can inflict on blood vessels.


## Resting Electrocardiographic Results (restecg)
**Description:** Results from an electrocardiogram during rest.  
**Role in Risk Assessment:** Abnormalities in ECG readings can indicate heart issues, including hypertrophy or ischemia.

### Values
- **0: Normal**
  - **Explanation**: Indicates no significant electrical abnormalities, suggesting a lower risk of heart disease.
- **1: ST-T wave abnormality**
  - **Explanation**: These abnormalities can indicate ischemia, or reduced blood flow to the heart, suggesting an increased risk of heart disease.
- **2: Left ventricular hypertrophy**
  - **Explanation**: Often a response to prolonged high blood pressure or other conditions that demand more from the heart muscle, associated with an increased risk of heart disease.



## Maximum Heart Rate Achieved (thalach)
Description: The maximum heart rate the patient achieved during exercise.
Role in Risk Assessment: A lower than expected maximum heart rate during exercise is inversely associated with cardiovascular mortality, indicating a higher risk of heart disease.

### Values and Scoring
- **Above 140 bpm**:
  - **Risk**: Low
  - **Value Points**: 0
  - **Explanation**: A normal or high maximum heart rate achieved during exercise, associated with better cardiovascular health and lower mortality risk.
- **121-140 bpm**:
  - **Risk**: Moderate
  - **Value Points**: 1
  - **Explanation**: Slightly below the optimal range but within a relatively safe margin; indicates a moderate risk of cardiovascular issues.
- **100-120 bpm**:
  - **Risk**: Moderately high
  - **Value Points**: 2
  - **Explanation**: Moderately below the normal range for maximum heart rate during exercise, suggesting increased cardiovascular risk.
- **Below 100 bpm**:
  - **Risk**: High
  - **Value Points**: 3
  - **Explanation**: Significantly lower than expected maximum heart rate; associated with a high risk of cardiovascular mortality. Indicates potential heart dysfunction or inadequate cardiovascular response to exercise.

### Prognostic Importance
- Both the maximum heart rate achieved during exercise and the difference between this and resting heart rate have strong prognostic implications for cardiovascular health.
- Lower exercise heart rates, particularly those below 100 bpm, are linked to significantly increased risks of cardiovascular death, independent of other conventional coronary risk factors such as cholesterol levels, blood pressure, and smoking status.
- Men in the lowest quartile of heart rate difference (the smallest increase from resting to maximum heart rate) exhibit the highest risk, emphasizing the importance of a robust heart rate response during exercise.

### Conclusions
Maximal exercise-induced heart rate and the difference between this and resting heart rate provide valuable predictive information about cardiovascular mortality risks in middle-aged individuals. Monitoring these metrics can be crucial for early detection of cardiovascular conditions and guiding preventive measures.


## Exercise Induced Angina (exang)
**Description:** Whether exercise induced angina (chest pain).  
**Role in Risk Assessment:** Experiencing angina during exercise is a significant indicator of coronary artery disease.

### Values
- **0**: No
  - **Explanation**: No occurrence of chest pain during exercise suggests a lower likelihood of significant coronary artery disease.
- **1**: Yes
  - **Explanation**: Presence of angina during exercise is a strong indicator of existing coronary artery disease, reflecting an inability of the coronary arteries to supply sufficient blood to the heart muscle during increased activity.

## ST Depression (oldpeak)
Description: ST depression on an ECG indicates a downward shift in a specific part of the heart's electrical signal. This change often suggests a problem with blood flow to the heart muscle, which could be due to conditions like angina or a heart attack. Doctors use this finding, along with other clinical information, to assess a patient's heart health and determine the appropriate treatment.
Role in Risk Assessment: ST depression can indicate myocardial ischemia, increasing heart disease risk.

### Values and Scoring
- **ST Depression < 1 mm**:
  - **Risk**: Low
  - **Value Points**: 0
  - **Explanation**: Minimal or no ST depression, typically indicating no significant myocardial ischemia under normal conditions.
- **ST Depression 1-2 mm**:
  - **Risk**: Moderate
  - **Value Points**: 1
  - **Explanation**: Mild ST depression, suggesting possible myocardial ischemia that may not be immediately life-threatening but could warrant further investigation.
- **ST Depression 2-3 mm**:
  - **Risk**: High
  - **Value Points**: 2
  - **Explanation**: Moderate ST depression, likely indicating more significant myocardial ischemia. This level requires clinical attention to address potential underlying heart issues.
- **ST Depression > 3 mm**:
  - **Risk**: Very High
  - **Value Points**: 3
  - **Explanation**: Severe ST depression, a critical indicator of substantial myocardial ischemia. This condition suggests a high risk of heart disease and necessitates immediate medical intervention.


## Slope of the Peak Exercise ST Segment (slope)
**Description:** The slope of the ST segment during peak exercise.  
**Role in Risk Assessment:** The slope can help in evaluating the severity of ischemic heart disease.

### Values
- **0**: Upsloping
  - **Explanation**: Generally considered normal or indicative of less severe disease.
- **1**: Flat
  - **Explanation**: Can indicate more significant heart disease, often seen in conditions that lead to reduced blood flow during exercise.
- **2**: Downsloping
  - **Explanation**: Often associated with severe ischemia and a high risk of heart disease, indicating significant obstruction to blood flow.


## Number of Major Vessels Colored by Fluoroscopy (ca)
Description: This metric indicates the number of major coronary arteries that can be seen filled with dye during a fluoroscopic angiogram. This test helps in identifying blockages in the arteries.
Role in Risk Assessment: A greater number of visible vessels typically indicates more severe coronary artery disease.

### Values and Scoring
- **0 vessels**:
  - **Risk**: Low
  - **Value Points**: 0
  - **Explanation**: No major coronary arteries are visible, suggesting no significant blockages or coronary artery disease.
- **1 vessel**:
  - **Risk**: Moderate
  - **Value Points**: 1
  - **Explanation**: One major coronary artery is visible, indicating some blockages, which may suggest mild to moderate coronary artery disease.
- **2 vessels**:
  - **Risk**: High
  - **Value Points**: 2
  - **Explanation**: Two major coronary arteries are visible, suggesting moderate to severe coronary artery disease.
- **3 vessels**:
  - **Risk**: Very High
  - **Value Points**: 3
  - **Explanation**: Three major coronary arteries are visible, indicating extensive coronary artery disease and a higher risk of significant cardiac events.

## Thalassemia (thal)
Description: Thalassemia is a genetic blood disorder that affects the body's ability to produce hemoglobin and red blood cells, impacting oxygen transport and flow.
Role in Risk Assessment: Certain types of thalassemia, particularly those that affect hemoglobin's effectiveness, can increase the risk of heart complications.

### Values and Scoring
- **Normal (3)**:
  - **Risk**: Low
  - **Value Points**: 0
  - **Explanation**: Normal hemoglobin function, no impact on heart disease risk from thalassemia.
- **Fixed defect (1)**:
  - **Risk**: Moderate
  - **Value Points**: 1
  - **Explanation**: A fixed defect in hemoglobin, leading to chronic but stable conditions that may slightly increase the risk of heart complications.
- **Reversible defect (6)**:
  - **Risk**: High
  - **Value Points**: 2
  - **Explanation**: A reversible defect in hemoglobin function that can lead to significant fluctuations in oxygen transport, increasing the risk of heart complications under stress or strain.



## Objective

By integrating discrete mathematics and statistical methods learned in class, we aim to create a predictive model that accurately quantifies an individual's risk level for heart disease. The ultimate vision for this tool is to develop a software application that can be readily used by individuals or healthcare professionals to assess risks and prioritize preventative healthcare measures effectively.

## Potential Impact

This tool has the potential to significantly impact how individuals and healthcare providers approach heart disease prevention. By offering a comprehensive analysis of various risk factors, it enables a proactive approach to health and wellness, encouraging lifestyle adjustments and interventions that can substantially reduce the risk of heart disease.

