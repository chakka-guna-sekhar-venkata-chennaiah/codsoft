import pandas as pd 
import numpy as np 
from source.exception import custom_exception
from source.loggers import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
import sys
from source.components.transformation import transformation_config
from source.components.transformation import transformation
from source.components.model_training import model_training_config
from source.components.model_training import model_training
@dataclass
class dataloadingconfig:
    train_data_path=os.path.join('artifacts','train_data.csv')
    test_data_path=os.path.join('artifacts','test_data.csv')
    raw_data_path=os.path.join('artifacts','data.csv')

class dataloading:
    def __init__(self):
        self.data_loading=dataloadingconfig()
    
    def initiate_data_loading(self):
        logging.info('Data loading is started')
        try:
            df=pd.read_csv('notebook/titanic.csv')
            df.drop(columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)

            logging.info('Reading the dataset as a dataframe')

            os.makedirs(os.path.dirname(self.data_loading.train_data_path),exist_ok=True)

            df.to_csv(self.data_loading.raw_data_path,index=False,header=True)
            logging.info('Train test split started')
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=0)

            train_data.to_csv(self.data_loading.train_data_path,index=False,header=True)
            test_data.to_csv(self.data_loading.test_data_path,index=False,header=True)

            logging.info('Data loading is completed')

            return(
                self.data_loading.train_data_path,
                self.data_loading.test_data_path
            )

        except Exception as e:
         raise custom_exception(e,sys)

if __name__=='__main__':
    data_load=dataloading()
    train_path,test_path=data_load.initiate_data_loading()

    data_transformation=transformation()
    train_array,test_array,_=data_transformation.initiate_transformer_object(train_path,test_path)

    modeltrainer=model_training()
    modeltrainer.initiate_model_training(train_array,test_array)

