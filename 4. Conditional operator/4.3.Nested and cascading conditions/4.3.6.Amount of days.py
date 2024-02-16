# Amount of days
# Given the serial number of the month (1,2,…, 12). 
# Write a program that displays the number of days in this month. Assume that the year is not a leap year.
# Note. Try to write a program so that it contains no more than three conditions.

# Количество дней
# Дан порядковый номер месяца (1,2,…, 12). 
# Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
# Примечание. Постарайтесь написать программу так, чтобы в ней было не более трех условий.

m = int(input())  #сколько дней в месяце
if m == 2:
    print('28')
elif m == 4 or m == 6 or m == 9 or m == 11:
    print('30')
else:
    print('31')

# Sample Input 1:
# 12
# Sample Output 1:
# 31
# Sample Input 2:
# 5
# Sample Output 2:
# 31
# Sample Input 3:
# 2
# Sample Output 3:
# 28
