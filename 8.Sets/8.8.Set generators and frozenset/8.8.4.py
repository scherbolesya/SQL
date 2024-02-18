# Используя генератор множеств, дополните приведенный код так, чтобы получить множество, 
# содержащее первую букву каждого слова (в нижнем регистре) списка words. 
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

# Using a set generator, complete the following code to produce a set containing 
# the first letter of each word (in lowercase) in the words list. 
# Print the result on one line in alphabetical order, separating elements with one space character.

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
chars = {c[0].lower() for c in words} 
print(*sorted(chars))
