from src.TextSummarization.logging import logger
from src.TextSummarization.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.TextSummarization.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.TextSummarization.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipepine = DataIngestionTrainingPipeline()
    data_ingestion_pipepine.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e