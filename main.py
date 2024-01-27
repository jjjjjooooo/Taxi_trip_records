from src.pipeline.stage_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_data_transformation import DataTransformationTrainingPipeline
from src.pipeline.stage_data_visualization import DataVisualizationTrainingPipeline
from src.utils.logger import logger
from src.utils.exception import CustomException
import sys


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)


STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)


STAGE_NAME = "Data Visualization"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_visualization = DataVisualizationTrainingPipeline()
    data_visualization.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)
