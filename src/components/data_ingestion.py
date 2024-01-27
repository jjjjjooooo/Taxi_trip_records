from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utils import *
from src.constants import *
from src.entity import DataIngestionConfig

from datetime import datetime
import requests
import time
import sys


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_parquet_file(self, year: int, month: int, max_retries):
        """
        Downloads a Parquet file for a specific year and month.

        Parameters:
            - year (int): The year for which to download the Parquet file.
            - month (int): The month for which to download the Parquet file.
            - target_directory (str): The directory where the file should be saved.

        Raises:
            - CustomException: If an error occurs during the download.
        """
        parquet_url = self.config.source_URL.format(year, month)

        for i in range(max_retries):
            try:
                response = requests.get(parquet_url)
            except Exception as e:
                backoff_factor = 0.3
                wait_time = backoff_factor * (2**i)
                time.sleep(wait_time)
                logger.error(
                    f"Connection error with yellow_tripdata_{year}-{month:02d}.parquet: {str(e)}"
                )

        if response.status_code == 200:
            file_name = self.config.local_data_name.format(year, month)
            file_path = os.path.join(self.config.root_dir, file_name)

            with open(file_path, "wb") as file:
                file.write(response.content)

            logger.info(
                "File {} successfully downloaded to {}".format(
                    file_name, self.config.root_dir
                )
            )
        else:
            logger.info(
                f"Failed to download yellow_tripdata_{year}-{month:02d}.parquet. Status code: {response.status_code}"
            )
            raise CustomException(
                f"Failed to download yellow_tripdata_{year}-{month:02d}.parquet. Status code: {response.status_code}",
                sys,
            )

    def extract_date(self, filename):
        """
        Extracts the year and month information from the filename.

        Parameters:
            - filename (str): The name of the file.

        Returns:
            - tuple: A tuple containing the year and month extracted from the filename.
        """
        year_month = filename.split("_")[2].split(".")[0]
        year = int(year_month.split("-")[0])
        month = int(year_month.split("-")[1])
        return year, month

    def download_missing_parquet_files(self):
        """
        download_missing_parquet_files function to manage the download process for missing Parquet files.
        """

        # Get the list of existing files and their corresponding dates
        files = os.listdir(self.config.root_dir)
        existing_dates = set(map(self.extract_date, files))

        # Generate a list of all possible dates up to the current month
        start_year = 2009
        full_dates = [
            (year, month)
            for year in range(start_year, datetime.now().year + 1)
            for month in range(1, 13)
            if (year, month) < (datetime.now().year, datetime.now().month)
        ]

        # Check for missing files and download them
        for date in full_dates:
            if date not in existing_dates:
                try:
                    self.download_parquet_file(
                        date[0], date[1], self.config.max_retries
                    )
                except Exception as e:
                    logger.error(str(e))
