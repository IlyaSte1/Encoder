from itertools import product
import json


def add_symbol(symbol: str):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789,. ' + symbol
    a = [i for i in product('.-', repeat=6)][:len(alphabet)]
    data = {}
    for i in range(len(a)):
        data[f'{alphabet[i]}'] = ''.join(a[i])

    with open('data.json', 'w') as write_file:
        json.dump(data, write_file)


def encode(text: str) -> str:
    s = ''
    text_1 = text.upper()
    with open('data.json', 'r') as read_file:
        d = dict(json.load(read_file))

    for i in text_1:
        s += d.get(i)

    return s


def decode(text: str) -> str:
    s = ''
    temp_list = []
    with open('data.json', 'r') as read_file:
        d = dict(json.load(read_file))
    
    for i in range(len(text) // 6):
        t = text[:6]
        text = text[6:]
        if t:
            temp_list.append(t)
        else:
            continue

    for i in temp_list:
        for k, v in d.items():
            if i == v:
                s += k

    return s
