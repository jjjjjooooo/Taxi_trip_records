from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_name: str
    max_retries: int


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    lowest_speed: float
    highest_speed: float
    shortest_trip_distance: float
    shortest_trip_duration: int
    least_cost: float


@dataclass(frozen=True)
class DataVisualizationConfig:
    root_dir: Path
    data_path: Path
    rolling_days: int
    monthly_average_file_name: str
    rolling_average_file_name: str
