# Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
# Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь
# result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
# Примечание 2. Для получения ASCII кода символа используйте функцию ord().
# Примечание 3. Выводить содержимое словаря result не нужно.

# Complete the given code using a generator to obtain a dictionary result in which the key is the string - an element of the words list, 
# and the value is a list of the corresponding ASCII codes of the characters in this string.
# Note 1: If the list of words looked like: words = ['yes', 'hello'], then the result would be a dictionary
# result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
# Note 2: To get the ASCII code of a character, use the ord() function.
# Note 3: There is no need to display the contents of the result dictionary.

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {word: [ord(i) for i in word] for word in words}
