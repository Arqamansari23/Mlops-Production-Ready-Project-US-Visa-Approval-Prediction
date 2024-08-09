# this file config_entity specify all paths where thing like raw data train data test data model are stored 


import os
from us_visa.constants import *
from dataclasses import dataclass
from datetime import datetime



TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name:str=PIPELINE_NAME
    artitact_dir:str=os.path.join(ARTIFACT_DIR,TIMESTAMP)
    timestamp:str=TIMESTAMP


training_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()


@dataclass
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artitact_dir, DATA_INGESTION_DIR_NAME)   
    # Full path: artifact/<TIMESTAMP>/data_ingestion
    
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    # Full path: artifact/<TIMESTAMP>/data_ingestion/feature_store/usvisa.csv
    
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    # Full path: artifact/<TIMESTAMP>/data_ingestion/ingested/train.csv
    
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    # Full path: artifact/<TIMESTAMP>/data_ingestion/ingested/test.csv
    
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    # Train-test split ratio: 0.2
    
    collection_name: str = DATA_INGESTION_COLLECTION_NAME
    # Collection name: visa_data



