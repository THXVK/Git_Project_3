def replacement_filter(text):
    return text.replace("а", "ы")


def shouting_filter(text):
    return text.upper()


def encoder_filter(text):
    alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ""
    for i in text:
        location = alphabet_RU.find(i)
        new_location = location + 2
        if i in alphabet_RU:
            result += alphabet_RU[new_location]
        else:
            result += i
    return result


def decoder_filter(text):
    alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ""
    for i in text:
        location = alphabet_RU.find(i)
        new_location = location - 2
        if i in alphabet_RU:
            result += alphabet_RU[new_location]
        else:
            result += i
    return result

filters = {  # Словарь с описанием фильтров
    1: {"name": "Replace Filter",
        "description": "Преобразует текст в формат Replace (заменяет букву 'а' на... , а впрочем догадайся сам.).\n",
        "function": replacement_filter},
    2: {"name": "SHOUTING Filter",
        "description": "Преобразует текст в формат SHOUTING (Кричащий текст).\n",
        "function": shouting_filter},
    3: {"name": "Encoder Filter",
        "description": "Преобразует текст в формат Encoder (Шифрует текст шифром Цезаря. Писать прописными русскими буквами 'ПРИВЕТ!').\n",
        "function": encoder_filter},
    4: {"name": "Decoder Filter",
        "description": "Преобразует текст в формат Decoder (Расшифровывает текст, зашифрованный шифром Цезаря. Писать прописными русскими буквами 'ПРИВЕТ!').\n",
        "function": decoder_filter},
    0: {"name": "Выход"}
}