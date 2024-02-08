# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.
# Write a program that calculates the sum, difference, and product of two integers entered from the keyboard.

# Sample Input 3:
# 10
# 10
# Sample Output 3:
# 10 + 10 = 20
# 10 - 10 = 0
# 10 * 10 = 100

a = int(input())
b = int(input())

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
