# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

import requests
import json


def data_dict(listname):
    dict = {}
    __temp = listname.split()
    temp = __temp.split(",")
    print(temp)
    for item in temp:
        _temp = item.split(":")
        key = _temp[0]
        if key in dict:
            dict[key].append(_temp[1])
        else: dict[key] = [_temp[0]]
    return dict



URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20230322&json"

response = requests.get(URL)
__dict = str(response.text)
print("Origins", __dict)
_dict = __dict.split()
print("_dict", _dict)
dict1 = _dict[2].split(",")
print("dict1", dict1)
dict = data_dict(dict1)