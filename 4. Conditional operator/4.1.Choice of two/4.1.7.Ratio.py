# Ratio
# Write a program that checks that for a given four-digit number the following relation holds: the sum of the first and last digits is equal to the difference of the second and third digits.
  
# Соотношение 
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input()) 
a = num % 10
b = (num % 1000)//100
c = (num % 100)//10
d = num //1000

if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')


# Sample Input 1:
# 1614
# Sample Output 1:
# ДА
# Sample Input 2:
# 1234
# Sample Output 2:
# НЕТ
# Sample Input 3:
# 7911
# Sample Output 3:
# ДА
