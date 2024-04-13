def read_txt(file_path: str) -> str:
    """
    function, which reads text from .txt file

    It takes as arguments path to the file
    It returns what the file contains
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        return file.read()

def write_txt(data: str, file_path: str) -> None:
    """
    function, which writes text in .txt file

    It takes as arguments data, which it should write into, and path to the file
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(data))

def count_character_frequency(text: str) -> dict:
    """
    function, which counts the frequency of every symbol in the text file

    It takes as arguments the text
    It returns the dictionary with frequencies
    """
    character_frequency = {}
    text = text.lower()
    for char in text:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1
    
    total_characters = len(text)
    character_index = {char: count / total_characters for char, count in character_frequency.items()}
    
    return dict(character_index)

coded = read_txt("D:\оиб\лаба 1\original text.txt")
character_index = count_character_frequency(coded)

write_txt(character_index, "D:/оиб/лаба 1/freq.txt")
