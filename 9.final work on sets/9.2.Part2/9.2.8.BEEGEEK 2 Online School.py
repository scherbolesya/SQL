# BEEGEEK 2 Online School
# Every student studying at the BEEGEEK online school studies either mathematics or computer science, or both of these subjects. 
# The head of the school has lists of students studying each subject.
# Write a program that allows a teacher to find out how many students are studying math only.
# Note. It is guaranteed that there are no namesakes among BEEGEEK school students.

# Онлайн-школа BEEGEEK 2
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета. У руководителя школы есть списки изучающих каждый предмет.
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m,n = int(input()), int(input())
mat = set()
inf = set()
for i in range(m):
    mat.add(input())
for i in range(n):
    inf.add(input())
print(len(mat - inf))

Sample Input 1:
2
3
Хохлов
Фадеев
Ершов
Ушаков
Хохлов
Sample Output 1:
1
Sample Input 2:
5
1
Игнатов
Мухин
Сафонов
Калашников
Демин
Рыбаков
Sample Output 2:
5
Sample Input 3:
2
4
Блинов
Жданов
Бобров
Жданов
Некрасов
Блинов
Sample Output 3:
0
