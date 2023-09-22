
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_training import ModelTrainingPipeline


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


STAGE_NAME = "Data Transformation"

try:
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<\n")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<\n")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"\n>>>>>>>>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e