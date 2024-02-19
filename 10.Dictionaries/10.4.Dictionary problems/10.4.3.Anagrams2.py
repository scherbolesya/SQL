# Anagrams 2
# The program receives two proposals as input. Write a program that determines whether they are anagrams or not. Your program should ignore case, punctuation, and spaces.
# Note. In addition to words, the text may contain spaces and punctuation marks .,!?:;-. There are no other characters in the text.

# Анаграммы 2
# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. 
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

result, result1 = {}, {}
for key in input().lower():
    if key.isalpha():
        result[key] = result.get(key,0) + 1
for key in input().lower():
    if key.isalpha():
        result1[key] = result1.get(key,0) + 1  
print('YES' if result == result1 else 'NO')

Sample Input 1:
Вижу зверей
Живу резвей
Sample Output 1:
YES
Sample Input 2:
Когда увидимся
тогда и свидимся
Sample Output 2:
NO
Sample Input 3:
С мая весной
сам я не свой
Sample Output 3:
YES
