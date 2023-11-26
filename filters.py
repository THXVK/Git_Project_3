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