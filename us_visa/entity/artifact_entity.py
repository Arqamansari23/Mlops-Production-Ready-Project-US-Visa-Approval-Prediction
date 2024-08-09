# this file defines the output types of all Pipelines 
from dataclasses import dataclass


# The Data Ingestion Pipeline returns the path of train and test data  
@dataclass
class DataIngestionReturnType:
    trained_file_path:str
    test_file_path:str





@dataclass
class DataValidationReturnType:
    validation_status:bool
    message: str
    drift_report_file_path: str



    
