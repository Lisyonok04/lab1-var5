import json
import os

import const


def read_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read()
    except Exception:
        print(Exception)


def write_txt(data: str, file_path: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(data))
    except Exception:
        print(Exception)


def count_character_frequency(text: str) -> dict:
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
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        print(Exception)


def encrypt(text: str, key: dict[str, str]) -> str:
    result = ""
    for lit in text:
        if lit in key.keys():
            result += key[lit]
        else:
            result += lit
    return result


def main() -> None:
    for dir in const.dirs:
        text = read_txt(os.path.join(dir, const.origin_file))
        key = read_json(os.path.join(dir, const.key_file))
        resulting = encrypt(text, key)
        write_txt(resulting, os.path.join(dir, const.result_file))


if __name__ == "_main_":
    main()
