# ML Projects

## 1. Air Foil prediction

## 2. Student_Performace_Prediction
 Aim:- To predict maths score of a student 
 
### Components
#### <a href="https://github.com/seruvuri/ML-Projects/blob/main/Students_performance_prediction/src/components/data_ingestion.py" target="_blank">Data Ingestion</a>
  
    Things to do in data_ingestion.py component:

    1.Reading data from local or clipboard or database.

    2.Spliting the data into train and test data.

    3.Saving the train and test data to respective file path.

    4.Returing  test and train data path to next step i.e DataTransformation step to do transformations. 
    
#### <a href="https://github.com/seruvuri/ML-Projects/blob/main/Students_performance_prediction/src/components/data_transformation.py" target="_blank">Data Transformation</a>

    Things to do in data_transformation.py component

    1.Creating a class which is used to store the transformation pickle file 

    2.creating "get_data_transformer_object" function
        2.1)-getting the list of numerical and categorical features
        2.2)-creating piplines using "sklearn-Pipeline" library
            -> for Numerical features
                -for handeling missing values--by replacing with median
                 -for standard scaling
            ->Categorical features
                -for handeling missing values--by replacing with mode
                -for handeling categorical values --onehotencoding
                -for standard scaling

    3.column transformation
        -combining all the pipeleine using column transformation

    4.Initiating Data transformation
      4.1)-Reading Train and Test data from respective path
      4.2)-getting target column and numerical features
      4.3)-getting Training data input features and trainig data target features
      4.4)-performing fit_transform on trainig data and tranform on test data 

    5. Saving the "preprocessing_obj" to pickle file by using saving _obj function in utils file

    6.Combining data trasformation in data_ingestion file
    
#### <a href="https://github.com/seruvuri/ML-Projects/blob/main/Students_performance_prediction/src/components/model_trainer.py" target="_blank">Model Trainer</a>

     Things to do in model_trainer.py component
     
     1.creating class for string the model pickle file.
     
     2.Splitting the input data into X_trian,X_test,y_train,y_test.
     
     3.creating models list with different algorithms.
     
     4.Creating "evaluate_model" function in utils file
        ->training model foir test and train data 
        ->calculating r2_score for test and train model
        ->creating report.
        
     5.saving model in model.pkl.
     
     6.prediciting with X_test data using best model.

## Pipeline 

<a href="https://github.com/seruvuri/ML-Projects/blob/main/Students_performance_prediction/src/pipline/predict_pipline.py" target="_blank">Predict Pipeline</a>

    Things to do in predict_pipeline.py 
    
    1. creating Predictpipeline class 
        ->loading preprocessor pickle file
        ->loading model.pickle file for predictions 
    
    2.Creating CustomData class
        ->mapping the values given in html page to bacekd values
    
    3.creating get_data_as_frame function 
         ->use to return all the input in the form of dataframe because we train model using dataframe. 
  
