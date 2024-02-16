# Accessory 3
# Принадлежность 3

# Write a program that accepts an integer x and determines whether the given number belongs to the specified intervals from -30 to -2 and from 7 to 25.
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам от -30 до -2 и от 7 до 25.

x = int(input())     # принадлежность к участкам
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')
  
# Sample Input 1:
# -332
# Sample Output 1:
# Не принадлежит
# Sample Input 2:
# -30
# Sample Output 2:
# Не принадлежит
# Sample Input 3:
# -21
# Sample Output 3:
# Принадлежит
