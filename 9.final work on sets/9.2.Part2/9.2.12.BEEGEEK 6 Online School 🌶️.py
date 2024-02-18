# BEEGEEK 6 Online School 🌶️
# The head of the BEEGEEK online school wanted to know which of his students had attended all lessons since the beginning of the school year. 
# For each lesson there is a sheet with a list of students present.
# Write a program that determines the names of students who attended all lessons.
# Note 1. It is guaranteed that there are no namesakes among BEEGEEK school students.
# Note 2: It is guaranteed that at least one student attended all lessons.
  
# Онлайн-школа BEEGEEK 6 🌶️
# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. 
# Для каждого урока есть листок со списком присутствовавших учеников.
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
# Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
# Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.

m = int(input())
n = int(input())
set1 = {input() for _ in range(n)}
for i in range(m-1):
    n = int(input())
    a = {input() for _ in range(n)}
    set1 &= a
print(*sorted(set1), sep = '\n')

Sample Input 1:
2
4
Черкасов
Фокин
Самойлов
Устинов
2
Черкасов
Устинов
Sample Output 1:
Устинов
Черкасов
Sample Input 2:
1
5
Сахаров
Авдеев
Зверев
Селезнев
Нечаев
Sample Output 2:
Авдеев
Зверев
Нечаев
Сахаров
Селезнев
Sample Input 3:
3
3
Князев
Сафонов
Майоров
2
Князев
Майоров
1
Майоров
Sample Output 3:
Майоров
