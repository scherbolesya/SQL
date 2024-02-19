# Synonym dictionary
# You are given a dictionary consisting of pairs of synonymous words. There are no duplicate words in the dictionary. Write a program that, for one given word, determines its synonym.
# Note 1: It is guaranteed that a synonym for the entered word exists in the dictionary.
# Note 2: All words in the dictionary begin with a capital letter.

# Словарь синонимов
# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.
# Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.
# Примечание 2. Все слова в словаре начинаются с заглавной буквы.

result = {}
for i in range(int(input())):
    s, s1 =  input().split()
    result[s1] = s
    result[s] = s1
key = input()    
print(result[key])

Sample Input 1:
4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:
Beautiful
Sample Input 2:
3
Kind Affable
Intellect Mind
Popular Celebrated
Popular
Sample Output 2:
Celebrated
