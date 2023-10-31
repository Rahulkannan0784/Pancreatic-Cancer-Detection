from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('model.pkl')

@app.route('/')
def home():
    return render_template('cancer.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the values from the form
    age = request.form['age']
    sex = request.form['sex']
    PLasama_CA19_9 = request.form['PLasama_CA19_9']
    Creatine = request.form['Creatine']
    LYVE1 = request.form['LYVE1']
    REG18 = request.form['REG18']
    TFF1 = request.form['TFF1']
    REG1A = request.form['REG1A']
    FM = request.form['FM']

    # Check if any of the form fields are empty
    if not age or not sex or not PLasama_CA19_9 or not Creatine or not LYVE1 or not REG18 or not TFF1 or not REG1A or not FM:
        error_msg = 'All form fields are required!'
        return render_template('cancer.html', error_msg=error_msg)

    # Make a prediction
    prediction = model.predict([[age, sex, PLasama_CA19_9, Creatine, LYVE1, REG18, TFF1, REG1A, FM]])[0]

    # Display the prediction result
    if prediction == 0:
        result = 'No cancer detected'
    else:
        result = 'Cancer detected'

    return render_template('cancer.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
