# Triangle view
# Write a program that takes three positive numbers and determines the type of triangle whose side lengths are equal to the numbers entered.

# Вид треугольника
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

a, b, c = int(input()), int(input()), int(input())   #стороны  треугольника какие они
if a == b == c:
    print('Равносторонний')
elif a != b != c and a != c:
    print('Разносторонний')
else:
    print('Равнобедренный')

# Sample Input 1:
# 145
# 145
# 139
# Sample Output 1:
# Равнобедренный
# Sample Input 2:
# 59
# 59
# 59
# Sample Output 2:
# Равносторонний
# Sample Input 3:
# 890
# 199
# 700
# Sample Output 3:
# Разносторонний
