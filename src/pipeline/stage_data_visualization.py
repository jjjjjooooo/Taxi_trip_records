from src.config.config import ConfigurationManager
from src.components.data_visualization import DataVisualization


class DataVisualizationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_visualization_config = config.get_data_visualization_config()
        data_visualization = DataVisualization(config=data_visualization_config)
        data_visualization.execute_analysis("rolling_average")
        data_visualization.execute_analysis("monthly_average")
