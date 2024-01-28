import pytest
from unittest.mock import Mock, patch, mock_open
from src.entity import DataVisualizationConfig
import src.components.data_visualization as dv
import pandas as pd
import os


# Fixture for DataIngestionConfig
@pytest.fixture
def config():
    return DataVisualizationConfig(
        root_dir="data/",
        data_path="data/",
        monthly_average_file_name="monthly_average_trip_length.parquet",
        rolling_average_file_name="rolling_average_trip_length.parquet",
        rolling_days=45,
    )


# Fixture for DataIngestion instance
@pytest.fixture
def data_visualization(config):
    return dv.DataVisualization(config)


# Test Initialization
def test_initialization(data_visualization, config):
    assert data_visualization.config == config


# Test calculate_monthly_average
@patch("pandas.DataFrame.to_parquet")
@patch("os.listdir")
@patch("pyarrow.parquet.read_table")
def test_calculate_monthly_average(
    mock_read_table, mock_listdir, mock_to_parquet, data_visualization
):
    # Set up mocks
    mock_listdir.return_value = ["pruned-yellow_tripdata_2009-04.parquet"]
    mock_df = pd.DataFrame(
        {
            "date": ["2009-04-05", "2009-04-06"],
            "trip_duration": [100, 200],
            "trip_distance": [5, 8],
        }
    )
    mock_table = Mock()
    mock_table.to_pandas.return_value = mock_df
    mock_read_table.return_value = mock_table

    # Run the method under test
    data_visualization.calculate_monthly_average()

    # Assertions to ensure the method behaves as expected
    mock_listdir.assert_called_once_with(data_visualization.config.data_path)
    mock_read_table.assert_called()
    mock_to_parquet.assert_called_once_with(
        f"data/{data_visualization.config.monthly_average_file_name}", index=False
    )


# Test calculate_rolling_average
@patch("pandas.DataFrame.to_parquet")
@patch("os.listdir")
@patch("pyarrow.parquet.read_table")
def test_calculate_rolling_average(
    mock_read_table, mock_listdir, mock_to_parquet, data_visualization
):
    # Set up mocks
    mock_listdir.return_value = ["pruned-yellow_tripdata_2009-05.parquet"]
    mock_df = pd.DataFrame(
        {
            "date": ["2009-04-05", "2009-04-06"],
            "trip_duration": [100, 200],
            "trip_distance": [5, 8],
        }
    )

    mock_table = Mock()
    mock_table.to_pandas.return_value = mock_df
    mock_read_table.return_value = mock_table

    # Run the method under test
    data_visualization.calculate_rolling_average()

    # Assertions to ensure the method behaves as expected
    mock_listdir.assert_called_once_with(data_visualization.config.data_path)
    mock_read_table.assert_called()
    mock_to_parquet.assert_called_once_with(
        f"data/{data_visualization.config.rolling_average_file_name}", index=False
    )


# Test test_execute_analysis
@patch("os.path.exists")
@patch("os.listdir")
@patch("src.utils.utils.load_yaml")
@patch("builtins.open", new_callable=mock_open)
@patch(
    "src.components.data_visualization.DataVisualization.calculate_rolling_average"
)  # Example for a specific analysis type
@patch(
    "src.components.data_visualization.DataVisualization.plot_interactive_trip_length"
)
def test_execute_analysis(
    mock_plot_interactive,
    mock_calculate,
    mock_open,
    mock_load_yaml,
    mock_listdir,
    mock_exists,
    data_visualization,  # Assuming this is a fixture for your DataVisualization instance
):
    analysis_type = "rolling_average"  # Example analysis type
    file_path = os.path.join(
        data_visualization.config.root_dir, "existing_file_count.yaml"
    )
    analysis_file = os.path.join(
        data_visualization.config.root_dir, f"{analysis_type}_trip_length.parquet"
    )

    # Setup mocks
    mock_exists.return_value = False

    mock_listdir.return_value = [
        "file1.parquet",
        "file2.parquet",
    ]  # Two files in directory
    mock_load_yaml.return_value = {"file_count": 1}  # Current count is 1

    # Execute the method
    data_visualization.execute_analysis(analysis_type)

    # Verify file operations
    mock_load_yaml.assert_not_called()
    mock_open.assert_called_with(file_path, "w")

    # Verify correct analysis method is called
    mock_calculate.assert_called_once()

    # Verify plotting is called
    mock_plot_interactive.assert_called_with(analysis_file)
