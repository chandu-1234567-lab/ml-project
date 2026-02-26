import os
import sys
from src.logger import logging
import pandas as pd # type: ignore
from src.exception import custom
from sklearn.model_selection import train_test_split # type: ignore
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
class Ingestion:
    def __init__(self):
        self.Ingestion_Config=DataIngestionConfig()
    
    def data_initiate(self):
        logging.info("enter the data ingestion method or component")
        try:
            df=pd.read_csv(r"notebook\data\stud.csv") # type: ignore
            logging.info('Read the dataset as Dataframe ')
            os.makedirs(os.path.dirname(self.Ingestion_Config.train_data_path),exist_ok=True)
            df.to_csv(self.Ingestion_Config.raw_data_path,header=True,index=False)
            logging.info('Train test Split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.Ingestion_Config.train_data_path,index=False,header=True)
            test_set.to_csv(self.Ingestion_Config.test_data_path,index=False,header=True)
            logging.info('Ingestion is completed')
            return (
                self.Ingestion_Config.train_data_path,
                self.Ingestion_Config.test_data_path,
                )
            
        except:
            raise custom(e,sys) # type: ignore
if __name__=='__main__':
    obj=Ingestion()
    obj.data_initiate()