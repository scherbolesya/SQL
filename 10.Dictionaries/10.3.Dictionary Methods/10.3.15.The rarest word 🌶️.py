# The rarest word 🌶️
# A line of text is given as input to the program. Write a program that prints the word that occurs least frequently, case insensitively. 
# If there are several such words, print the one that is smaller in lexicographical order.
# Note 1. The program should not be case sensitive; the words apple and Apple should be perceived as the same.
# Note 2. A word is a sequence of letters. In addition to words, the text may contain spaces and punctuation marks .,!?:;-, which must be ignored. There are no other characters in the text.

# Самое редкое слово 🌶️
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

result = {}
text = input()
w = []
for word in text.split():
    w.append(word.lower().strip('.,;:-?!'))
s1 = set(i for i in w)
for i in s1:
    key = w.count(i)
    result[key] = result.get(key, []) + [i]
print(sorted(result[min(result.keys())])[0])

Sample Input 1:
home sweet home
Sample Output 1:
sweet
Sample Input 2:
home sweet home sweet.
Sample Output 2:
home
