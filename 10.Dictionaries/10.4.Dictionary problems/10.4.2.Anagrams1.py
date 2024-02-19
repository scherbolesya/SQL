# Anagrams 1
# An anagram is a word (phrase) formed by rearranging the letters that make up another word (or phrase). For example, the English words evil and live are anagrams.
# The program is given two words as input. Write a program that determines whether they are anagrams.

# Анаграммы 1
# Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.
# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

result = {}
result1 = {}
for key in input():
    result[key] = result.get(key, 0) + 1
    
for key in input():
    result1[key] = result1.get(key, 0) + 1
    
if result == result1:
    print('YES')
else:
    print('NO')

Sample Input 1:
thing
night
Sample Output 1:
YES
Sample Input 2:
cat
rat
Sample Output 2:
NO
Sample Input 3:
tea
eat
Sample Output 3:
YES
