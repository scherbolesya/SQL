# Перестановка цифр

# Дано трехзначное число abc, в котором все цифры различны. 
# Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
# Формат выходных данных
# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа, в следующем порядке (каждое на новой строке): 
# abc,acb,bac,bca,cab,cba.


#  Rearranging numbers

# Given a three-digit number abc in which all digits are different.
# Write a program that prints six numbers formed by rearranging the digits of a given number.
# The program should print six numbers formed by rearranging the digits of a given number, in the following order (each on a new line):
# abc,acb,bac,bca,cab,cba.

# abc,acb,bac,bca,cab,cba.
num = int(input())
c = num % 10
b = (num % 100) // 10
a = num // 100
print (a,b,c, sep='')
print (a,c,b, sep='')
print (b,a,c, sep='')
print (b,c,a, sep='')
print (c,a,b, sep='')
print (c,b,a, sep='')

# Sample Input 1:
# 123
# Sample Output 1:
# 123
# 132
# 213
# 231
# 312
# 321
# Sample Input 2:
# 987
# Sample Output 2:
# 987
# 978
# 897
# 879
# 798
# 789
