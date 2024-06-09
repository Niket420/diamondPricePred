import  os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## intialize the data ingestion configuration

@dataclass                                                #if u r using @dataclass ,then u dont need self variable to make class variable
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')         # to save the file train.csv in artifacts folder
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')




## create a data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()      # to get all the parameter of DataIngestionconfig
    
    def initiate_data_ingestion(self):                   #all details like reading a file,saving it ,will be stored here ,,main work will be done here
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)       # to make an artifact folder and raw_data file to store df dataframe
            df.to_csv(self.ingestion_config.raw_data_path,index=False)                            # to save that df in that folder

            logging.info("Train test split")

            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('ingestion ho gaya bhai')

            ## output is train and test data after ingestion

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )





        except Exception as e:
            logging.info(f'Error occured in Data ingestion config:{str(e)}')