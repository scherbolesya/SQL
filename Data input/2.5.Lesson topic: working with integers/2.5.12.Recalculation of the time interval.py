# Пересчет временного интервала

# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

# Recalculation of the time interval

# Write a program to convert the value of a time interval specified in minutes into a value expressed in hours and minutes.

# Sample Input 1:
# 150
# Sample Output 1:
# 150 мин - это 2 час 30 минут.

m = int(input())
h = m // 60
m1 = m % 60
print(m, 'мин - это', h, 'час', m1, 'минут.')
