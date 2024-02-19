# Дополните приведенный код, используя генератор, так чтобы получить словарь result , в котором ключом будет позиция числа в списке numbers (начиная с 0), а значением – его квадрат.
# Примечание. Выводить содержимое словаря result не нужно.

# Complete the code above using a generator to produce a dictionary result in which the key is the position of the number in the list numbers (starting at 0), and the value is its square.
# Note. There is no need to display the contents of the result dictionary.

numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {k: numbers[k]**2 for k in range(len(numbers))}
