import pickle 
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_app',methods=['POST'])
def predict_api():

    data=request.json['data']#since we use data as key in input we write 'data'
    print(data)
    new_data=[list(data.values())]# converting 1d array to 2d array 
    output=model.predict(new_data)[0]
    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():

    data=[float(x) for x in request.form.values()] #To retrive data from the html page
    final_features= [np.array(data)] # all the data from text box is saved in final_features and converting into 2 dimension
    print(data)
    
    output=model.predict(final_features)[0]
    print(output)
    return render_template('home.html',prediction_text="Airfoil pressure is {}".format(output)) 

if __name__== "__main__":
    app.run(debug=True)