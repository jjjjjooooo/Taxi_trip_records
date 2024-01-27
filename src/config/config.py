from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utils import *
from src.constants import *

from src.entity import DataIngestionConfig
from src.entity import DataTransformationConfig
from src.entity import DataVisualizationConfig


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = load_yaml(config_filepath)
        self.params = load_yaml(params_filepath)

        create_directories([self.config["artifacts_root"]])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        params = self.params["data_ingestion"]

        create_directories([config["root_dir"]])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_name=config["local_data_name"],
            max_retries=params["max_retries"],
        )

        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config["data_transformation"]
        params = self.params["data_transformation"]

        create_directories([config["root_dir"]])

        data_transformation_config = DataTransformationConfig(
            root_dir=config["root_dir"],
            data_path=config["data_path"],
            lowest_speed=params["lowest_speed"],
            highest_speed=params["highest_speed"],
            shortest_trip_distance=params["shortest_trip_distance"],
            shortest_trip_duration=params["shortest_trip_duration"],
            least_cost=params["least_cost"],
        )

        return data_transformation_config

    def get_data_visualization_config(self) -> DataVisualizationConfig:
        config = self.config["data_visualization"]
        params = self.params["data_visualization"]

        create_directories([config["root_dir"]])

        data_visualization_config = DataVisualizationConfig(
            root_dir=config["root_dir"],
            data_path=config["data_path"],
            rolling_days=params["rolling_days"],
            monthly_average_file_name=config["monthly_average_file_name"],
            rolling_average_file_name=config["rolling_average_file_name"],
        )

        return data_visualization_config
