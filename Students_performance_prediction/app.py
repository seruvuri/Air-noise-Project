from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler# we import Standard scaler to use pickel file
from src.pipline.predict_pipline import CustomData, Predictpipeline

application=Flask(__name__)

app=application

## routing for homePage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicteddata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') ## home.html has simple imput data fields that are needed to provide to model for predictions
    else:
        # when we post the request will have all the information so we read all the information from request
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')),

        )
        #the funcatoin is available in predict_pipeline.py which returns dataframe 
        pred_df=data.get_data_as_frame()
        print(pred_df)

        predict_pipeline=Predictpipeline()
        '''as soon as we call the predict function in prediction_pipeline.py it will trigger the functin 
        and do the transformation and predictions as mentinoed in it'''
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    # host ="0.0.0.0" will map to 127.0.1
    app.run(host="0.0.0.0",debug=True)
    

