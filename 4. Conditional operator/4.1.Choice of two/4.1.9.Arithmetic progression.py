# Write a program that determines whether three given numbers (in the given order) are consecutive terms of an arithmetic progression.
# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
a = int(input()) 
b = int(input())
c = int(input())
if (b - a) + b == c:
    print('YES')
else:
    print('NO')
# Sample Input 1:
# 1
# 2
# 3
# Sample Output 1:
# YES
# Sample Input 2:
# 1
# 2
# 4
# Sample Output 2:
# NO
# Sample Input 3:
# 2
# 4
# 8
# Sample Output 3:
# NO
