import json
import os


def read_json(file_path: str) -> object:
    """Read json for the given file

    Args:
        file_path (str): Location to the file

    Returns:
        object: The content of the file
    """
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def folder_path_exists(path: str) -> bool:
    """Does folder path exists
    
    Args:
        path (str): folder path location

    Returns:
        bool: True if the path exists
    """
    return os.path.isdir(path)

def file_path_exists(path: str) -> bool:
    """Does file exists
    
    Args:
        path (str): file location

    Returns:
        bool: True if the file exists
    """
    return os.path.isfile(path)
