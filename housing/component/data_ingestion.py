from housing.entity.config_entity import DataIngestionConfig
import sys, os
from housing.exception import HousingException
from housing.logger import logging

class Data_Ingestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e



    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
