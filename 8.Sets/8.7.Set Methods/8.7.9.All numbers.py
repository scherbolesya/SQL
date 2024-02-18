# All numbers
# The program is given two numbers as input. Write a program that determines whether 
#the first number contains all the digits contained in the second number (regardless of the repetition, that is, the number of digits) or not.

# Все цифры
# На вход программе подаются два числа. Напишите программу, которая определяет, 
#vвходят ли в запись первого числа все цифры, содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.

print('YES' if set(input()).issuperset(set(input())) else 'NO')

Sample Input 1:
123456789
657
Sample Output 1:
YES
Sample Input 2:
1254
1243
Sample Output 2:
NO
Sample Input 3:
12345678
999
Sample Output 3:
NO
