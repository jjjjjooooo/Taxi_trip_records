import os
import sys
import yaml
from src.utils.exception import CustomException
from src.utils.logger import logger
import dill
import pickle
from ensure import ensure_annotations
from pathlib import Path


@ensure_annotations
def load_yaml(file_path):
    """reads yaml file and returns

    Args:
        file_path (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return content
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def save_object(file_path: Path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as f:
            dill.dump(obj, f)
            logger.info(f"file: {file_path} saved successfully")
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def load_object(file_path):
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)

    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def read_yaml(filename: Path, key: str) -> int:
    try:
        with open(filename, "r") as file:
            data = yaml.safe_load(file)
            value = data.get(key)
        return value

    except Exception as e:
        raise CustomException(e, sys)
