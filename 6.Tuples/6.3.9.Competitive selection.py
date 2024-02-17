# Competitive selection
# Note 1: A student's grade is a natural number from 1 to 5.
# Note 2. It is guaranteed that in the class there is at least one good student (with a score of 4) or an excellent student (with a score of 5).

# Конкурсный отбор
# Напишите программу, которая выводит список хорошистов и отличников в классе.
# Примечание 1. Оценка ученика – это натуральное число от 1 до 5.
# Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист (обладатель оценки 4) или отличник (получивший 5).

n = int(input()) #Конкурсный отбор
d = [input().split() for i in range(n)]
d1 = []
for i in range(n):
    if int(d[i][1])>=4:
        d1.append(d[i])


for f in d:
    print(*f)
print()
for s in d1:
    print(*s)

# Sample Input 1:
# 3
# Гуев 3
# Чаниев 5
# Барсуков 2
# Sample Output 1:
# Гуев 3
# Чаниев 5
# Барсуков 2

# Чаниев 5

# Sample Input 2:
# 5
# Круглов 4
# Кузнецов 5
# Федин 4
# Тарасов 2
# Словецкий 3
# Sample Output 2:
# Круглов 4
# Кузнецов 5

# Федин 4
# Тарасов 2
# Словецкий 3
