# Список tuples содержит кортежи, состоящие из трех чисел.
# Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент каждого кортежа, а значением – кортеж из оставшихся двух элементов.
# Примечание. Выводить содержимое словаря result не нужно.

# The list of tuples contains tuples consisting of three numbers.
# Complete the following code using a generator to produce a dictionary result, where the key is the first element of each tuple and the value is the tuple of the remaining two elements.
# Note. There is no need to display the contents of the result dictionary.

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {i[0]: i[1:] for i in tuples}
