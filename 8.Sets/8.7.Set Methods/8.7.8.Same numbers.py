# Same numbers
# The program is given two numbers as input. Write a program to determine whether given numbers have identical digits.
# Одинаковые цифры
# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

print('YES' if (set(input())) & (set(input())) else 'NO')

Sample Input 1:
114
223
Sample Output 1:
NO
Sample Input 2:
1523
3678
Sample Output 2:
YES
Sample Input 3:
5543
3455
Sample Output 3:
YES
