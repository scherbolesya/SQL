# Only + 🌶️
# Только + 🌶️
# write a program that reads three numbers and calculates the sum of only positive numbers.
# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a = int(input()) 
b = int(input())
c = int(input())
if a >= 0:
    d = a
else:
    d = 0
if b >= 0:
    h = b
else:
    h = 0
if c >= 0:
    k = c
else:
    k = 0
print(d+h+k)

# Sample Input 1:
# 4
# -22
# 1
# Sample Output 1:
# 5
# Sample Input 2:
# 33
# 55
# 63
# Sample Output 2:
# 151
# Sample Input 3:
# -1
# 37
# 62
# Sample Output 3:
# 99
