#Урок 3. Функции. Словари
#1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
#"один"
#>>> num_translate("eight")
#"восемь"
#Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(stroka):
    if stroka == "one":
         return "один"
    elif stroka == "two":
         return "два"
    elif stroka == "three":
         return "три"
    elif stroka == "four":
         return "чотири"
    elif stroka == "five":
         return "п'ять"
    elif stroka == "six":
         return "шість"
    elif stroka == "seven":
         return "сім"
    elif stroka == "eight":
         return "вісім"
    elif stroka == "nine":
         return "дев'ять"
    elif stroka == "ten":
         return "десять"
    elif stroka == "zero":
         return "нуль"
    return None

def num_translate_adv(stroka):
    if stroka.lower() == "one":
         if stroka[0].islower():
             return "один"
         else: return "Один"
    elif stroka.lower() == "two":
         if stroka[0].islower():
            return "два"
         else: return "Два"
    elif stroka.lower() == "three":
         if stroka[0].islower():
            return "три"
         else: return "Три"
    elif stroka.lower() == "four":
        if stroka[0].islower():
            return "чотири"
        else: return "Чотири"
    elif stroka.lower() == "five":
        if stroka[0].islower():
            return "п'ять"
        else: return "П'ять"
    elif stroka.lower() == "six":
        if stroka[0].islower():
            return "шість"
        else: return "Шість"
    elif stroka.lower() == "seven":
        if stroka[0].islower():
            return "сім"
        else: return "Сім"
    elif stroka.lower() == "eight":
        if stroka[0].islower():
            return "вісім"
        else: return "Вісім"
    elif stroka.lower() == "nine":
        if stroka[0].islower():
            return "дев'ять"
        else: return "Дев'ять"
    elif stroka.lower() == "ten":
        if stroka[0].islower():
            return "десять"
        else: return "Десять"
    elif stroka.lower() == "zero":
        if stroka[0].islower():
            return "нуль"
        else: return "Нуль"
    return None

# dig = input()
dig = ""
print(
    num_translate(dig)
)
print(
    num_translate_adv(dig)
)

#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"], "П": ["Петр"]
#}

def thesaurus(list_name):
    dictionary = {}                         # створення пустого словника
    for item in list_name:                  # перебираємо кожний елемент зі списка імен
        key = item[0]                       # створюємо КЛЮЧ для словника з першої літери імені
        if key in dictionary:               # перевіряємо чи існує такий ключ в словнику
            dictionary[key].append(item)    # якщо існує - додаємо значення
        else: dictionary[key] = [item]      # якщо ні - створюємо новий ключ зі значенням імені
    return dictionary

# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }

def thesaurus_adv(list_name):
    dictionary = {}                         # створення пустого словника
    for item in list_name:                  # перебираємо кожний елемент зі списка
        _FIO = item.split(" ")              # розбиваємо строку на масив
        _familia = _FIO[1]                  # визначаємо фамілію за номером 1 в списку (0 - це ім'я)
        key = _familia[0]                   # визначаємо КЛЮЧ першою літерою фамілії
        if key in dictionary:
            dictionary[key].append(item)
        else: dictionary[key] = [item]
    return dictionary

list_name = input().split(", ")
print(list_name)
print(thesaurus_adv(list_name))


