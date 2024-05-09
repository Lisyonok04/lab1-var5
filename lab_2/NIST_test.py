import json
import math
import mpmath

from typing import Dict

from const import PATH, PI


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
    sum = 0
    for i in name:
                if i == "1":
                    sum -= 1
                else:
                    sum += 1
    s = abs(sum / math.sqrt(len(name)))
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
    sum = 0
    for i in range(n - 1):
        if name[i] != name[i + 1]:
            sum += 1
    p = math.erfc(abs(sum - 2 * n * units * (1 - units)) /
                       (2 * math.sqrt(2 * n) * units * (1 - units)))
    return p


def max_sequence(name: str) -> int:
    """
    The function searches for the maximum length of a
    sequence

    Args:
             name(str): path .json file
    Returns:
             maxline(int): longest sequence
    """
    maxline = 0
    count = 0
    for i in name:
        if i == "1":
            count += 1
            maxline = max(maxline, count)
        else:
            #maxline = max(maxline, count)
            count = 0
    return maxline


def longest_sequence(name: str) -> float:
    """The function analyzes for the longest sequence in block

    Args:
            name(str): random sequence

    Returns:
            p(float): P-value
    """
    max_len = {}
    length = len(name)
    v = {1: 0, 2: 0, 3: 0, 4: 0}
    for step in range(0, length, 8):
        block = name[step: step + 8]
        block_max_len = max_sequence(block)
        if block_max_len in max_len:
            max_len[block_max_len] += 1
        else:
            max_len[block_max_len] = 1
    for i in max_len:
        if i <= 1:
            v[1] += max_len[i]
        elif i == 2:
            v[2] += max_len[i]
        elif i == 3:
            v[3] += max_len[i]
        else:
            v[4] += max_len[i]
    xi_squared = 0
    for i in range(4):
            xi_squared += ((v[i + 1] - 16 * PI[i + 1]) ** 2) / (16 * PI[i + 1])
    p = mpmath.gammainc(3 / 2, xi_squared / 2)
    return p


def main() -> None:
    c = get_json(PATH)["C++"]
    java = get_json(PATH)["java"]
    print("results for C++: ")
    print(frequency(c))
    print(identical(c))
    print(longest_sequence(c))
    print("results for Java: ")
    print(frequency(java))
    print(identical(java))
    print(longest_sequence(java))
    

if __name__ == "__main__":
    main()
 