# Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка numbers, 
# а значением – отсортированный по возрастанию список всех его делителей начиная с 1.
# Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
# result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
# Примечание 2. Выводить содержимое словаря result не нужно. 

# Using the generator, complete the code above to produce a dictionary result , where the key is the list element numbers and 
# the value is an ascending-sorted list of all its divisors, starting with 1.
# Note 1: If the list of numbers had the form: numbers = [1, 6, 18], then the result would be a dictionary
# result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
# Note 2: There is no need to display the contents of the result dictionary.

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {number : [i for i in range(1,number+1) if number % i == 0] for number in numbers}
