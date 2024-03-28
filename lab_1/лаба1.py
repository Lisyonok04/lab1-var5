def read_txt(file_path: str) -> str:
    """
    function, which reads text from .txt file

    It takes as arguments path to the file
    It returns what the file contains
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        return file.read()


def count_character_frequency(text) -> dict:
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

text = "И7У24>2 >МР4ДД >М2ЕПЧЙМД48 О4ЙАИЛМrЕt48ДЕ2ЧММИЙtЕХ4МШ4Ф1МЙ>ХИЙМУ1УМРОЕУ<Д >МР4ДД >МУ1УМЕЪУШtЕО4ДД ФМИУПД41МИМЙЕ<ХУМ8t>ДУЛМЙ>ЕtУУМrt>РrЕ14П4>ЙИЛМ<ЙЕМР4ДД >МrtЕУ8ОЕРЛЙИЛМУИЙЕ<ДУХЕ2МУМrt>РЕИЙ4О1ЛКЙИЛМХЕ2rt>ИИЕtЧМОМ ОУР>МИУ2ОЕ14МД4РМД>ХЕЙЕt 2М41Ш4ОУЙЕ2Мt4ДАЫ>МО>ИАМrtЕЪ>ИИМИ74ЙУЛМД48 О41УМХЕРУtЕО4ДУ>2МУИЙЕ<ДУХ4МrЕИХЕ1АХЧМЕДЕМrtУ8О4ДЕМЧР41УЙ АМУ85 ЙЕ<ДЕИЙАМОМР4ДД ЩМД4МЕИДЕО>МУЩМrt>РИХ48Ч>2ЕИЙУМrЧЙ>2МУДЕПЕМrt>РИЙ4О1>ДУЛ МР4ДД ЩММЙЕМ>ИЙАМУЩМХЕРУtЕО4ДУЛМ84МРО4МrЕИ1>РДУЩМР>ИЛЙУ1>ЙУ ЛМХ4tЙУД4МД>ИХЕ1АХЕМУ82>ДУ14ИАМr>tОЕФМ14ИЙЕ<ХЕФМИЙ414МУР> ЛМt48Р>1УЙАМrtЕЪ>ИИМИ74ЙУЛМД4МРО4МО84У2ЕИОЛ84ДД ЩМrtЕЪ>ИИ4МХЕРУtЕО4ДУ>МД>rЕИt>РИЙО>ДДЕМОЕИrtЕУ8ОЕРЛЬ>>МИ74Й ФМrЕЙЕХМИУ2ОЕ1ЕОМУМ2ЕР>1УtЕО4ДУ>Мrt>РЕИЙ4О1ЛКЬ>>МОИКМД>Е5ЩЕРУ2ЧК МР1ЛМХЕРУtЕО4ДУЛМУДШЕt24ЪУК"
character_index = count_character_frequency(text)

for char, index in character_index.items():
    print(f"{char}, {index}")

text_de = "сжимаемые данные могут называться поразному строка файл текст или двоичные данные или оцифрованный сигнал с точки зрения теории предполагается что данные производятся источником и предоставляются компрессору в виде символа над некоторым алфавитом раньше весь процесс сжатия называли кодированием источника поскольку оно призвано удалить избыточность в данных на основе их предсказуемости путем иного представления данных то есть их кодирования за два последних десятилетия картина несколько изменилась первой ласточкой стала идея разделить процесс сжатия на два взаимосвязанных процесса кодирование непосредственно воспроизводяЬее сжатый поток символов и моделирование предоставляющее всю необходимую для кодирования информацию"
