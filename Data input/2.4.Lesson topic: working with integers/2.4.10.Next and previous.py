# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
# Write a program that reads an integer and then displays the next and previous integer with explanatory text.

a = int(input())
b = a + 1
c = a - 1
print('Следующее за числом', a, 'число:', b)
print('Для числа', a, 'предыдущее число:', c)
