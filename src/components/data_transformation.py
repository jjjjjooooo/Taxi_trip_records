import os
import sys
import pandas as pd
import pyarrow.parquet as pq
from src.utils.exception import CustomException
from src.utils.logger import logger
from src.constants import *
from src.entity import DataTransformationConfig
from dateutil.relativedelta import relativedelta


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def find_column_name(self, columns, keyword):
        """Find a column name containing a specific keyword."""
        return next((col for col in columns if keyword in col), None)

    def calculate_trip_duration_and_speed(self, df):
        """Calculate trip duration in seconds and speed in miles per hour."""
        df["trip_duration"] = (
            pd.to_datetime(df["dropoff_datetime"], errors="coerce")
            - pd.to_datetime(df["pickup_datetime"], errors="coerce")
        ).dt.total_seconds()
        df["speed"] = df["trip_distance"] / (df["trip_duration"] / 3600)
        return df

    def data_cleaning(self):
        """
        Processes and cleans the taxi trip data files stored in a specified directory.

        This function iterates through each file in the data directory, performs cleaning and transformation operations, and saves the processed data to a new file. Cleaning operations include renaming columns, dropping rows with missing values, and calculating additional metrics like trip duration and speed.

        For each file:
        - Skips processing if the pruned file already exists in the output directory.
        - Renames columns related to pickup datetime, dropoff datetime, and total amount for consistency.
        - Drops rows with missing values in critical columns.
        - Calculates the trip duration in seconds and the speed in miles per hour.
        - Filters the data based on predefined configuration thresholds for speed, trip distance, trip duration, and total amount.
        - Saves the cleaned and pruned data as a new Parquet file in the output directory.

        Exceptions are logged and raised as CustomException for further handling.

        Raises:
            CustomException: If any error occurs during the data cleaning process.
        """
        try:
            for filename in os.listdir(self.config.data_path):
                input_path = os.path.join(self.config.data_path, filename)
                output_path = os.path.join(self.config.root_dir, f"pruned-{filename}")

                start_date = pd.to_datetime(
                    filename.split("_")[-1].replace(".parquet", "") + "-01"
                )
                end_date = start_date + relativedelta(months=1)

                start_date_str = start_date.strftime("%Y-%m-%d")
                end_date_str = end_date.strftime("%Y-%m-%d")

                if os.path.exists(output_path):
                    logger.info(f"Skipping existing file: {output_path}")
                    continue

                logger.info(f"Processing file: {filename}")
                df = pq.read_table(input_path).to_pandas().rename(columns=str.lower)

                df = df.rename(
                    columns={
                        self.find_column_name(df.columns, "pickup"): "pickup_datetime",
                        self.find_column_name(
                            df.columns, "dropoff"
                        ): "dropoff_datetime",
                        self.find_column_name(df.columns, "total"): "total_amount",
                    }
                )

                df = df.dropna(
                    subset=[
                        "pickup_datetime",
                        "dropoff_datetime",
                        "total_amount",
                        "trip_distance",
                    ]
                )
                df = self.calculate_trip_duration_and_speed(df)

                pruned_df = df.query(
                    f"{self.config.lowest_speed} < speed < {self.config.highest_speed} and "
                    f"trip_distance > {self.config.shortest_trip_distance} and "
                    f"trip_duration > {self.config.shortest_trip_duration} and "
                    f"total_amount > {self.config.least_cost} and "
                    f"'{start_date_str}' <= pickup_datetime < '{end_date_str}'"
                ).copy()

                pruned_df["date"] = pd.to_datetime(pruned_df["pickup_datetime"]).dt.date

                pruned_df.to_parquet(output_path, index=False)
                logger.info(f"Pruned data saved to {output_path}")

        except Exception as e:
            logger.error(f"Error during data cleaning: {e}")
            raise CustomException(f"Data cleaning failed: {e}", sys)
