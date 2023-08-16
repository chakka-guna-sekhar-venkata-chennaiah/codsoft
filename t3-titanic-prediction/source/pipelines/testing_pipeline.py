import sys
import os
import pandas as pd
from source.loggers import logging
from source.exception import custom_exception
from source.utlis import load_object
class prediction_pipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaling=preprocessor.transform(features)
            prediction=model.predict(data_scaling)
            return prediction
            
        except Exception as e:
            raise custom_exception(e,sys)


    
class custom_data:
    def __init__(self,
        Pclass:str,
        Sex:str,
        Age:float,
        Sibsip:float,
        Parch:float,
        Fare:float,
        Embarked:str

        ):
        self.Pclass=Pclass
        self.Sex=Sex
        self.Age=Age
        self.Sibsip=Sibsip
        self.Parch=Parch
        self.Fare=Fare
        self.Embarked=Embarked
       

    def get_data_as_a_dataframe(self):
        try:
            custom_data_input_dict={
            'Pclass':[self.Pclass],
            'Sex':[self.Sex],
            'Age':[self.Age],
            'Sibsip':[self.Sibsip],
            'Parch':[self.Parch],
            'Fare':[self.Fare],
            'Embarked':[self.Embarked]

            




            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise custom_exception(e,sys)
