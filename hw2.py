#   1. Выяснить тип результата выражений:
#   15 * 3
#   15 / 3
#   15 // 2
#   15 ** 2
print("Тип операції 15 * 3 є", type(15*3))
print("Тип операції 15 / 3 є", type(15/3))
print("Тип операції 15 // 2 є", type(15//2))
print("Тип операції 15 ** 2 є", type(15**2))

# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# вирішення другої половини завдання
i = 0
_length = len(spisok)
while i < _length:
    if spisok[i].upper() == spisok[i]:
        spisok.insert(i + 1, "'")
        spisok.insert(i, "'")
        print(i)
        print(spisok)
        _length = _length+2
        if i + 3 <= _length:
            i = i+3
        else: i=_length
    else: i = i + 1
string = " ".join(spisok)
print(string)

# вирішення другої половини завдання. ver 2
i = 0

while i < _length:
    if spisok[i].upper() == spisok[i]:
        spisok[i] = "'" + spisok[i] + "'"
        i = i +1
#        spisok.insert(i, "'")
#        print(i)
        print(spisok)
#        _length = _length+2
#        if i + 3 <= _length:
#            i = i+3
#        else: i=_length
#    else: i = i + 1
string = " ".join(spisok)
print(string)


