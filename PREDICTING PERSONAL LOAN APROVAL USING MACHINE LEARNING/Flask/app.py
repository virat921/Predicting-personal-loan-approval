import os
import h5py
from flask import Flask, render_template, request
import numpy as np
import pandas
import pickle

app = Flask(__name__)
model = h5py.File('loan.h5', 'r')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/predict',methods=["POST","GET"])
def submit():
    input_feature = [int(x) for x in request.form.values()]
    input_feature = [np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome' 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    data = pandas.DataFrame(input_feature, columns=names)
    print(data)

    prediction=model.predict(data)
    print(prediction)
    prediction = int(prediction)

    if(prediction == 0):
        return render_template("predict.html", result="Loan will not be Approved")
    else:
        return render_template("predict.html", result="Loan will be Approved")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    port = int(os.environ.get('PORT', 5000))
    #app.run(dubug=True)