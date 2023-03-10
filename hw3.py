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
#    dictionary = {}
    list_word = ""
    i = 0
    while i < len(list_name):
        stroka = list_name[i]
        list_word = list_word + stroka[0]
        print(list_word)
        i = i + 1
    char_list = list(list_word)
    return char_list

list_name = input().split(", ")
print(list_name)
print(thesaurus(list_name))