import json
import math
import mpmath

from typing import Dict

from const import PATH

def get_json(name: str) -> Dict[str, str]:
    """Function reads the json-file at the specified path 
    and saves it to a variable

    Returns:
        _type_: data from json-file
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The file was not found.")


def frequency(name: str) -> float:
    """
    The function checks if the sequence is random enough

    Args:
            name(str): path to .json file

    Returns:
            p(float): P-value
    """
    s = abs(sum(1 if i == "1" else -1 for i in name)) / math.sqrt(len(name))
    p = math.erfc(s / math.sqrt(2))
    return p


def identical(name: str) -> float:
    """
    The test is to find all sequences of the same bits 
    and to determine how often the change from "1" to "0" 
    and back occurs using the formula.

    Args:    
            name(str): path .json file

    Returns:
            p(float): P-value
    """
    n = len(name)
    units = name.count("1") / n
    if abs(units - 0.5) >= 2 / math.sqrt(n):
        return 0
    v = sum(0 if name[i] == name[i + 1] else 1 for i in range(n - 1))
    p = math.erfc(abs(v - 2 * n * units * (1 - units)) /
                       (2 * math.sqrt(2 * n) * units * (1 - units)))
    return p


def main() -> None:
    c = get_json(PATH)["C++"]
    java = get_json(PATH)["java"]
    #print(frequency(c))
    #print(frequency(java))
    print(identical(c))
    print(identical(java))


if __name__ == "__main__":
    main()
 