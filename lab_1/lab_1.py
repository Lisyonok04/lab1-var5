import json
import os

import const


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


def write_txt(data: str, file_path: str) -> None:
    """Function writes data into the file at the specified path

    Args:
        data (str): the data which needs to be into the file
        file_path (str): path to the file where data was saved
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(data))
    except Exception:
        print(Exception)


def count_character_frequency(text: str) -> dict:
    """Function calculates the index of the frequency of characters found in a given text

    Args:
        text (str): The text analysed for the frequency index

    Returns:
        dict: key - a symbol, value - the index of the frequency
    """
    character_frequency = {}
    text = text.lower()
    for char in text:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

    total_characters = len(text)
    character_index = {char: count / total_characters for char,
                       count in character_frequency.items()}

    return dict(character_index)


def read_json(file_path: str) -> dict[str:str]:
    """Function reads the json-file at the specified path and saves it to a variable

    Returns:
        _type_: data from json-file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        print(Exception)


def text_process(text: str, key: dict[str, str]) -> str:
    """Function processes the text using a key

    Args:
        text (str): text for cyphering
        key (dict[str, str]): key for cyphering

    Returns:
        str: encrypted text
    """
    result = ""
    for lit in text:
        if lit in key.keys():
            result += key[lit]
        else:
            result += lit
    return result


def main() -> None:
    for dir in const.DIRS:
        text = read_txt(os.path.join(dir, const.ORIGIN_FILE))
        key = read_json(os.path.join(dir, const.KEY_FILE))
        resulting = text_process(text, key)
        write_txt(resulting, os.path.join(dir, const.RESULT_FILE))


if __name__ == "_main_":
    main()
