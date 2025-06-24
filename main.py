from src.TextSummarization.logging import logger
from src.TextSummarization.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipepine = DataIngestionTrainingPipeline()
    data_ingestion_pipepine.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e