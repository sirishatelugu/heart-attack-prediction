from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open("df.pkl", 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['age'])

        Gender = request.form['Gender']
        if Gender == "Male":
            Gender = 1
       	else:
            Gender = 0

        cp=request.form['cp']
        if cp =="typical angina":
            cp=0
        elif cp=="atypical angina":
            cp=1
        elif cp=="non-anginal pain":
            cp=2
        elif cp=="asymptomatic":
            cp=3

       	trtbps=request.form['trtbps']

        chol=request.form['chol']
	
        fbs=request.form['fbs']
        
        if(fbs=='True'):
            fbs=1
        else:
            fbs=0
	
        restecg=request.form['restecg']
        if(restecg=='normal'):
            restecg=0
        elif(restecg=='abnormal'):
            restecg=1
        elif(restecg=='definite'):
            restecg=2

        thalach=int(request.form['thalachh'])

        exng=request.form['exng']
        if(exng=='Yes'):
            exng=1
        elif(exng=='No'):
            exng=0

        oldpeak=float(request.form['oldpeak'])

        slp=int(request.form['slp'])

        css=int(request.form['caa'])

        thall=request.form['thall']
        if(thall=='normal'):
            thall=0
        elif(thall=='fixed'):
            thall=1
        elif(thall=='reversal'):
            thall=2

        prediction=model.predict(([[Age,Gender,cp,trtbps, chol, fbs, restecg, thalach, exng, oldpeak, slp, css, thall]]))
        
  	#return render_template('index.html',OUTPUT=prediction)
        #print(prediction)
        if(prediction):
            return render_template('index.html',OUTPUT="More Chance of Heart Attack")
        else:
            return render_template('index.html',OUTPUT="Less Chance Of Heart Attack")
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

