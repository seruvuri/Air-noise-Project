''' Things to do in data_ingestion component:

1.Reading data from local or clipboard or database
2.Spliting the data into train and test data
3.Saving the train and test data to respective file path
4.Returing  test and train data path to next step i.e DataTransformation step to do transformations  
'''



import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split


'''This module provides a decorator and functions for automatically 
adding generated special methods such as __init__() and __repr__() to user-defined classes.'''
from dataclasses import dataclass# used to create class variables
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

'''In data ingestion component we need inputs for data ingestion i.e 
where to save the train data 
save the test data and raw data'''


@dataclass 
class DataIngestionConfig:
    #inputs to data ingestion to save the train , test and raw data
    train_data_path: str=os.path.join('artifacts','train.csv')# all the data ingestion output will be saved in artifacts folder
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()# saving the DataIngestionConfig variables in ingestion_config variable

    ''' "initiate_data_ingestion" is used to read the data if it is saved in any database i.e mongodb etc. 
    we create client in "utils.py" and we can read it in the below function '''
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
            #cerating directory
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,header=True)
            logging.info("train_test_split is initated")

            #splitting the data into train test split
            train_set,test_set=train_test_split(df,test_size=0.2, random_state=42)
            
            #saving the train data to train data directory in artifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            #saving test data to respective folder in artifacts folder
            test_set.to_csv(self.ingestion_config.test_data_path)
            
            logging.info("Ingestion of the data is completed")
            
            #we pass this informatin to data tranformation to do take the below points and start data transformation
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    # combined data transformation
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))




