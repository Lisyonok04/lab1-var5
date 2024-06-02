from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import logging
import json


def write_txt(data: str, file_path: str) -> None:
    """Function writes data into the file at the specified path

    Args:
        data (str): the data which needs to be into the file
        file_path (str): path to the file where data was saved
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception:
        print(Exception)

def read_txt(file_path: str) -> str:
    """Function reads the file at the specified path and saves it to a variable

    Args:
        file_path (str): Path to a file

    Returns:
        str: a variable contains data from the file
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read()
    except Exception:
        print(Exception)

def write_symmetric_key(key: bytes, filename: str) -> None:
    """Function writes a symmetric key into a file

    Args:
        key (bytes): The symmetric key to write.
        filename (str): The name of the file to write the key to.
    """
    try:
        with open(filename, 'wb') as f:
            f.write(key)
    except Exception as e:
        logging.error(f'Error writing symmetric key to file: {e}')

