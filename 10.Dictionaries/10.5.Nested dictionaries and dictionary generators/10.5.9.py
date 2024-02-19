# Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.
# Примечание. Выводить содержимое словаря result не нужно.

# Complete the following code using a generator to produce a result dictionary consisting of all the months dictionary elements in which the key and value have been swapped.
# Note. There is no need to display the contents of the result dictionary.

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {value: key for key, value in months.items()}
