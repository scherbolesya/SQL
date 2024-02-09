# Трехзначное число

# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трехзначного числа.

# Three digit number

# Write a program that calculates the sum and product of the digits of a positive three-digit number.

# Sample Input 2:
# 333
# Sample Output 2:
# Сумма цифр = 9
# Произведение цифр = 27

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print ('Сумма цифр =', a + b + c)
print ('Произведение цифр =', a * b * c)
