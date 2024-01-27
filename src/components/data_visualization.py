import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyarrow.parquet as pq
from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utils import *
from src.constants import *
import yaml
from src.entity import DataVisualizationConfig
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class DataVisualization:
    def __init__(self, config: DataVisualizationConfig):
        self.config = config

    def load_data(self, file):
        df = pq.read_table(file).to_pandas()
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)
        return df

    def plot_static_trip_length(self, file_path):
        df = self.load_data(file_path)

        fig, ax1 = plt.subplots(figsize=(10, 6))
        sns.lineplot(
            data=df, x=df.index, y="average_trip_distance", ax=ax1, color="tab:red"
        )
        ax1.set_ylabel("Average Trip Distance [mile]", color="tab:red")
        ax1.set_xlabel("Date")
        ax2 = ax1.twinx()
        sns.lineplot(
            data=df, x=df.index, y="average_trip_duration", ax=ax2, color="tab:blue"
        )
        ax2.set_ylabel("Average Trip Duration [s]", color="tab:blue")
        plt.show()

    def plot_interactive_trip_length(self, file_path):
        df = self.load_data(file_path)

        folder_name, file_name = os.path.split(file_path)
        analysis_type = file_name.split("_")[-4].capitalize()

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["average_trip_distance"],
                name="Average Trip Distance",
                line=dict(color="red"),
            ),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["average_trip_duration"],
                name="Average Trip Duration",
                line=dict(color="blue"),
            ),
            secondary_y=True,
        )

        fig.update_layout(
            title_text=f"Trend Analysis: {analysis_type} Average of Trip Lengths for Yellow Taxis in New York City"
        )
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(
            title_text="Average trip distance [mile]",
            secondary_y=False,
            title_font=dict(color="red"),
        )
        fig.update_yaxes(
            title_text="Average trip duration [s]",
            secondary_y=True,
            title_font=dict(color="blue"),
        )
        fig.show()

    def calculate_monthly_average(self):
        try:
            monthly_averages = []
            for file_name in os.listdir(self.config.data_path):
                logger.info(f"Processing file: {file_name}")
                df = self.load_data(os.path.join(self.config.data_path, file_name))
                monthly_avg = df[["trip_duration", "trip_distance"]].mean()
                monthly_avg["date"] = (
                    file_name.split("_")[-1].replace(".parquet", "") + "-01"
                )
                monthly_averages.append(monthly_avg)

            df_monthly = pd.DataFrame(monthly_averages).rename(
                columns={
                    "trip_duration": "average_trip_duration",
                    "trip_distance": "average_trip_distance",
                }
            )
            df_monthly.to_parquet(
                os.path.join(
                    self.config.root_dir, self.config.monthly_average_file_name
                ),
                index=False,
            )
            logger.info(
                f"Monthly average trip length saved to {self.config.monthly_average_file_name}"
            )
        except Exception as e:
            logger.error(f"An error occurred during processing: {e}")
            raise CustomException(f"Processing monthly average failed: {e}", sys)

    def calculate_rolling_average(self):
        try:
            daily_averages = []
            for file_name in os.listdir(self.config.data_path):
                logger.info(f"Processing file: {file_name}")
                df = self.load_data(os.path.join(self.config.data_path, file_name))
                day_avg = df.resample("D")[["trip_duration", "trip_distance"]].mean()
                daily_averages.append(day_avg)

            combined_daily = pd.concat(daily_averages, ignore_index=False).sort_index()
            combined_daily["average_trip_distance"] = (
                combined_daily["trip_distance"]
                .rolling(window=self.config.rolling_days, min_periods=1)
                .mean()
            )
            combined_daily["average_trip_duration"] = (
                combined_daily["trip_duration"]
                .rolling(window=self.config.rolling_days, min_periods=1)
                .mean()
            )
            combined_daily.reset_index(inplace=True)
            combined_daily.to_parquet(
                os.path.join(
                    self.config.root_dir, self.config.rolling_average_file_name
                ),
                index=False,
            )
            logger.info(
                f"Rolling average trip length saved to {self.config.rolling_average_file_name}"
            )
        except Exception as e:
            logger.error(f"An error occurred during processing: {e}")
            raise CustomException(f"Processing rolling average failed: {e}", sys)

    def execute_analysis(self, analysis_type):
        file_path = os.path.join(self.config.root_dir, "existing_file_count.yaml")
        current_count = 0
        if os.path.exists(file_path):
            current_count = load_yaml(Path(file_path)).get("file_count", 0)
        file_count = len(os.listdir(self.config.data_path))

        if current_count < file_count or not os.path.exists(
            os.path.join(self.config.root_dir, f"{analysis_type}_trip_length.parquet")
        ):
            analysis_method = getattr(self, f"calculate_{analysis_type}")
            analysis_method()
            with open(file_path, "w") as file:
                yaml.dump({"file_count": file_count}, file)
            logger.info(
                f"{analysis_type.replace('_', ' ').title()} analysis completed and plotted."
            )
            self.plot_interactive_trip_length(
                os.path.join(
                    self.config.root_dir, f"{analysis_type}_trip_length.parquet"
                )
            )

        else:
            self.plot_interactive_trip_length(
                os.path.join(
                    self.config.root_dir, f"{analysis_type}_trip_length.parquet"
                )
            )
