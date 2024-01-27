import requests
import os
import sys
import unittest
from unittest.mock import patch, Mock, mock_open

# from src.utils.exception import CustomException


def download_parquet_file(year: int, month: int):
    parquet_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{:04d}-{:02d}.parquet".format(
        year, month
    )
    response = requests.get(parquet_url)

    if response.status_code == 200:
        file_name = "yellow_tripdata_{:04d}-{:02d}.parquet".format(year, month)
        file_path = os.path.join("artifacts/data_ingestion", file_name)

        with open(file_path, "wb") as file:
            file.write(response.content)

    # else:
    #     raise CustomException(
    #         f"Failed to download yellow_tripdata_{year}-{month:02d}.parquet. Status code: {response.status_code}",
    #         sys,
    #     )


@patch("requests.get")
@patch("builtins.open", new_callable=mock_open)
def test_download_parquet_file(mock_file_open, mock_get):
    # Mock for successful response
    mock_response_success = Mock()
    mock_response_success.status_code = 200
    # mock_response_success.content = b"file content"
    mock_get.return_value = mock_response_success

    # Test success case
    download_parquet_file(2020, 3)
    mock_file_open.assert_called_once()
    mock_get.assert_called_with(
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet"
    )


if __name__ == "__main_-":
    unittest.main()
