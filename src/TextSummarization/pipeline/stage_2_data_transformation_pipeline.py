from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.components.data_transformation import DataTransformation
from src.TextSummarization.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
                
    
