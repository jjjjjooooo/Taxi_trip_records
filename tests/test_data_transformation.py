import pytest
from unittest.mock import Mock, patch
from src.entity import DataTransformationConfig
import src.components.data_transformation as dt
import pandas as pd


# Fixture for DataIngestionConfig
@pytest.fixture
def config():
    return DataTransformationConfig(
        root_dir="data/",
        data_path="data/",
        lowest_speed=10,
        highest_speed=100,
        shortest_trip_distance=1,
        shortest_trip_duration=300,
        least_cost=10,
    )


# Fixture for DataIngestion instance
@pytest.fixture
def data_transformation(config):
    return dt.DataTransformation(config)


# Test Initialization
def test_initialization(data_transformation, config):
    assert data_transformation.config == config


# Test find_column_name
def test_find_column_name(data_transformation):
    columns = ["pickup_date", "dropoff_date", "total_amount"]
    assert data_transformation.find_column_name(columns, "pickup") == "pickup_date"
    assert data_transformation.find_column_name(columns, "dropoff") == "dropoff_date"


# Test calculate_trip_duration_and_speed
def test_calculate_trip_duration_and_speed(data_transformation):
    df = pd.DataFrame(
        {
            "pickup_datetime": ["2021-01-01 00:00:00", "2021-01-01 00:10:00"],
            "dropoff_datetime": ["2021-01-01 00:15:00", "2021-01-01 00:30:00"],
            "trip_distance": [1.5, 3],
        }
    )
    result = data_transformation.calculate_trip_duration_and_speed(df)
    assert "trip_duration" in result.columns
    assert "speed" in result.columns
    assert result.loc[0, "trip_duration"] == 900
    assert result.loc[1, "speed"] == 9


# Test test_data_cleaning
@patch("pandas.DataFrame.to_parquet")
@patch("os.listdir")
@patch("os.path.exists")
@patch("pyarrow.parquet.read_table")
def test_data_cleaning(
    mock_read_table,
    mock_exists,
    mock_listdir,
    mock_to_parquet,
    data_transformation,
    monkeypatch,
):
    # Create a real DataFrame for the test
    df_mock = pd.DataFrame(
        {
            "pickup_datetime": [
                "2010-02-02 10:00:00",
            ],
            "dropoff_datetime": [
                "2010-02-02 10:30:00",
            ],
            "total_amount": [15],
            "trip_distance": [10],
        }
    )

    # Create a mock PyArrow Table or similar object
    mock_table = Mock()
    mock_table.to_pandas.return_value = df_mock

    # Set up the other mocks
    mock_listdir.return_value = ["yellow_tripdata_2010-02.parquet"]
    mock_exists.return_value = False
    mock_read_table.return_value = mock_table

    # Mock logger to avoid side effects
    monkeypatch.setattr("src.utils.logger.logger", Mock())

    # Call the data_cleaning method
    data_transformation.data_cleaning()

    # Assertions
    mock_listdir.assert_called_once_with(data_transformation.config.data_path)
    mock_exists.assert_any_call("data/pruned-yellow_tripdata_2010-02.parquet")
    mock_read_table.assert_called_once_with("data/yellow_tripdata_2010-02.parquet")
    mock_to_parquet.assert_called_once_with(
        "data/pruned-yellow_tripdata_2010-02.parquet", index=False
    )
