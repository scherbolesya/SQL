# Merging dictionaries 🌶️
# Слияние словарей 🌶️

# Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, 
# каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.
# Write a merge() function that merges dictionaries into one common one. The function must accept a list of dictionaries 
# and return a dictionary, each key of which contains a set (set data type) of unique values collected from all dictionaries of the passed list.

# Примечание 1. Следующий программный код:
# Note 1. The following program code:
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# создает словарь:
# creates a dictionary:
result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# Примечание 2. Вызывать функцию merge() не нужно, требуется только реализовать. 
# Примечание 3. Слияние пустых словарей должно быть пустым словарем.
# Note 2: There is no need to call the merge() function, it just needs to be implemented.
# Note 3: Merging empty dictionaries must be an empty dictionary.

def merge(values):      # values - это список словарей
    a = {}
    for i in range (len(values)):
        for key, value in values[i].items():
            a[key] = a.get(key, []) + [value]
            
    for key, value in a.items():
        a[key] = set(value)
        
    
    return a
