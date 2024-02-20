# Query string
# Строка запроса
# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:
# Query string is the part of the URL containing the keys and their values. It starts after the question mark and goes to the end of the address. For example:

# https://beegeek.ru?name=timur     # строка запроса: name=timur

# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
# If there are several parameters in the query string, they are separated by the ampersand character &:

# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 

# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.
# Write a function build_query_string() that takes a dictionary with parameters as input and returns a query string formed from these parameters.

# Примечание 1. В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.
# Примечание 2. Следующий программный код:
# Note 1: The resulting string must sort the parameters in the lexicographic order of the dictionary keys.
# Note 2: The following program code:

# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

# должен выводить:
# should output:

# age=28&name=timur
# game=2&sport=hockey&time=17

# Примечание 3. Вызывать функцию build_query_string() не нужно, требуется только реализовать. 
# Note 3: There is no need to call the build_query_string() function, it just needs to be implemented.

def build_query_string(params):
    a = sorted([k+'='+ str(v) for k, v in params.items()])
    return '&'.join(a)
