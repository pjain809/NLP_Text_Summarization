
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"

try:
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<\n")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e
