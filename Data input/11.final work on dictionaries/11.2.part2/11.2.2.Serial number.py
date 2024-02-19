# Дана строка текста на русском языке, состоящая из слов и символов пробела. 
# Словом считается последовательность букв, слова разделены одним пробелом или несколькими.
# Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. 
# Для первого вхождения слова программа выведет 1, для второго вхождения того же слова — 2 и т. д.
# Примечание. Количество чисел должно совпадать с количеством слов исходного текста.

# Given a line of text in Russian, consisting of words and space characters. A word is a sequence of letters; words are separated by one or more spaces.
# Write a program that determines for each word the serial number of its occurrence in the text in exactly this form, taking into account case. 
# For the first occurrence of a word, the program will output 1, for the second occurrence of the same word, 2, etc.
# Note. The number of numbers must match the number of words in the source text.

a = {}
for key in input().split():
    a[key] = a.get(key, 0) + 1
    print(a[key], end=' ')

Sample Input 1:
прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
Sample Output 1:
1 1 2 1 1 2 1 2 3 1
Sample Input 2:
Привет что делаешь что нового что с работой как там с деньгами
Sample Output 2:
1 1 1 2 1 3 1 1 1 1 2 1
