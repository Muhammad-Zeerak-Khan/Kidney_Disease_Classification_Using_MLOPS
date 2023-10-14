import os 
from box.exceptions import BoxValueError
import yaml
from Kidney_Tumor_Classification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path) : path to the yaml file.

    Raise:
        ValueError : if yaml file is empty.

    Returns:
        ConfigBox : ConfigBox type object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml File : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    
    except Exception as e:
        raise e
           

@ensure_annotations
def create_directories(path_to_directories : list, verbose=True) -> None:
    """
    Creates directories provided in the directories_list.

    Args:
        path_to_directories (list) : list of directories to be created.
        ignore_log (bool, optional) : ignore if multiple directories are to be created. Defaults to False.

    """           
    for path in path_to_directories:
        os.makedirs(path, exists_ok=True)
        if verbose:
            logger.info(f"Directory : {path} created successfully")

@ensure_annotations
def save_json(path : Path, data: dict) -> None:
    """
    Saves a dictionary to a json file.

    Args:
        path (Path) : path to the json file.
        data (dict) : dictionary to be saved in a json file.

    """
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    logger.info(f"Json File : {path} saved successfully")

@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    """
    Loads a json file and returns a ConfigBox object.

    Args:
        path (Path) : path to the json file.

    Returns:
        ConfigBox : data as class attributes instead of a dictionary.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Json File : {path} loaded successfully")
            return ConfigBox(data)
        
    except Exception as e:
        raise e
    
@ensure_annotations
def save_bin(data : Any, path: Path) -> None:
    """
    Saves data to a binary file.

    Args:
        data (Any) : data to be saved.
        path (Path) : path to the binary file.

    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary File : {path} saved successfully")
    except Exception as e:
        raise e

@ensure_annotations
def load_bin(path : Path) -> Any:
    """
    Loads data from a binary file.

    Args:
        path (Path) : path to the binary file.

    Returns:
        Any : data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary File : {path} loaded successfully")
        return data
    except Exception as e:
        raise e
    
@ensure_annotations
def get_size(path : Path) -> str:
    """
    Returns the size of a file in Kilobytes.

    Args:
        path (Path) : path to the file.

    Returns:
        str : size of the file in bytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} Kb"

def decode_image(img_string : str, filename : str):
    img_data = base64.b64decode(img_string)
    try:
        with open(filename, 'wb') as f:
            f.write(img_data)
            f.close()
    except Exception as e:
        raise e        

def encode_image_to_base64(cropped_image_path):
    try:
        with open(cropped_image_path, 'rb') as f:
            img_data = f.read()
            img_string = base64.b64encode(img_data)
            return img_string
    except Exception as e:
        raise e