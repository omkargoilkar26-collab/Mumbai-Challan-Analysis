import pandas as pd
import numpy as np 
import os
from sqlalchemy import create_engine
import sqlite3
import logging
import time

logging.basicConfig(
    filename="logs/traffic.log",
    level=logging.DEBUG,
    format="%(asctime)s -- %(levelname)s -- %(message)s",
    filemode="a"
)



engine = create_engine('sqlite:///traffic.db')

def ingest_db(df,table_name,engine):
    '''This funtion will insert csv data into db'''
    df.to_sql(table_name, con= engine, if_exists='replace',index=False,chunksize=5000)


def load_raw_data():
    '''This funtion will load raw csv data and covert it into dataframe'''
    start = time.time()
    for file in os.listdir():
        if '.csv' in file:
            df = pd.read_csv(file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info(f'***********Ingestion Completed***********')
    logging.info(f'Total time taken {total_time} minutes')
            
if __name__ == '__main__':
    load_raw_data()