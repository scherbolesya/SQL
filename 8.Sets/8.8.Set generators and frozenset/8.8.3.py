# Используя генератор множеств, дополните приведенный код так, чтобы получить множество, 
# содержащее уникальные значения списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
# Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.
# Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:

# Using a set generator, complete the following code to produce a set containing the unique values of the items list. 
# The result is displayed on one line, in an ordered form, separating elements with one space character.
# Note 1: Please note that some list elements are numbers, and some are strings, and strings must be treated as numbers.
# Note 2: To display the elements of a set in an ordered form, use the following code:

print(*sorted(myset))

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(c) for c in items}
print(*sorted(myset))
