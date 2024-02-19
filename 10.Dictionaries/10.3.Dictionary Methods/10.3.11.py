# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2: если ключ есть в обоих словарях, 
# добавьте его в результирующий словарь со значением, равным сумме соответствующих значений из первого и второго словаря; 
# если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим значением. Результирующий словарь необходимо присвоить переменной result.
# Примечание. Выводить содержимое словаря result не нужно.

# Complete the above code so that it combines the contents of the two dictionaries dict1 and dict2: if the key is in both dictionaries, 
# add it to the resulting dictionary with a value equal to the sum of the corresponding values from the first and second dictionaries; 
# if the key is in only one of the dictionaries, add it to the resulting dictionary with its current value. The resulting dictionary must be assigned to the result variable.
# Note. There is no need to display the contents of the result dictionary.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = dict1.copy()
for key in dict2:
    result[key] = result.get(key, 0) + dict2[key]
