import pytest
from unittest.mock import Mock, patch, mock_open
from src.entity import DataIngestionConfig
import src.components.data_ingestion as di


# Fixture for DataIngestionConfig
@pytest.fixture
def config():
    return DataIngestionConfig(
        source_URL="http://api.example.com/{:04d}-{:02d}.parquet",
        local_data_name="{:04d}_{:02d}.parquet",
        root_dir="data/",
        max_retries=1,
    )


# Fixture for DataIngestion instance
@pytest.fixture
def data_ingestion(config):
    return di.DataIngestion(config)


# Test Initialization
def test_initialization(data_ingestion, config):
    assert data_ingestion.config == config


# Test download_parquet_file
@patch("requests.get")
@patch("builtins.open", new_callable=mock_open)
# These decorators ensure that the actual external calls (HTTP requests and file operations) are not executed during the test.
def test_download_parquet_file(mock_open, mock_get, data_ingestion):
    mock_response = Mock()

    # Test success case
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    data_ingestion.download_parquet_file(2018, 2, 1)
    mock_get.assert_called_with("http://api.example.com/2018-02.parquet")
    mock_open.assert_called_with("data/2018_02.parquet", "wb")

    # Reset mocks for failure test
    mock_open.reset_mock()
    mock_get.reset_mock()

    # Test failure case
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    with pytest.raises(Exception):
        data_ingestion.download_parquet_file(2018, 2, 1)
        mock_open.assert_not_called()


# Test extract_date
def test_extract_date(data_ingestion):
    year, month = data_ingestion.extract_date("yellow_trip_2020-01.parquet")
    assert year == 2020 and month == 1


# Test download_missing_parquet_files
@patch("src.components.data_ingestion.DataIngestion.download_parquet_file")
@patch("os.listdir")
def test_download_missing_parquet_files(mock_listdir, mock_download, data_ingestion):
    mock_listdir.return_value = ["example_data_2007-01.parquet"]
    data_ingestion.download_missing_parquet_files()
    assert mock_download.call_count == 180
