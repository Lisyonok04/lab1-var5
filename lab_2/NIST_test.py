import json
import math
import mpmath

from typing import Dict

from const import PATH

def get_json(name: str) -> Dict[str, str]:
    """Function reads the json-file at the specified path and saves it to a variable

    Returns:
        _type_: data from json-file
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The file was not found.")


def frequency_bitwise_test(name: str) -> float:
    """
    The function checks if the sequence is random enough

    Args:
            name(str): path to .json file

    Returns:
            float: P-value
    """
    s = abs(sum(1 if i == "1" else -1 for i in name)) / math.sqrt(len(name))
    return math.erfc(s / math.sqrt(2))

def main() -> None:
    name = get_json(PATH)["java"]
    print(frequency_bitwise_test(name))


if __name__ == "__main__":
    main()
 