# Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.
# Примечание. Выводить содержимое словаря result не нужно.
# Complete the code below so that the result variable stores a dictionary in which the keys are numbers from 1 to 15 (inclusive), and the values are the squares of the keys.
# Note. There is no need to display the contents of the result dictionary.

result = {key : key*key for key in range(1,16)}
