# Accessory 1
# Принадлежность 1
# Write a program that accepts an integer x and determines whether it belongs to the range from -1 to 17.
# Напишите программу, которая принимает целое число x и определяет, принадлежит к промежутку от -1 до 17. 

x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')


# Sample Input 1:
# 2
# Sample Output 1:
# Принадлежит
# Sample Input 2:
# -790
# Sample Output 2:
# Не принадлежит
# Sample Input 3:
# -1
# Sample Output 3:
# Не принадлежит
