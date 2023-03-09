#Урок 3. Функции. Словари
#1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
#"один"
#>>> num_translate("eight")
#"восемь"
#Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.



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

print(
    num_translate_adv(input())
)

#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"], "П": ["Петр"]
#}

def thesaurus(list_name):