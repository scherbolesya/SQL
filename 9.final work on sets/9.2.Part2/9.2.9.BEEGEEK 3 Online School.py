# BEEGEEK 3 Online School
# Every student studying at the BEEGEEK online school studies either mathematics or computer science, or both of these subjects. 
# The head of the school has lists of students studying each subject.
# Write a program that allows a teacher to find out how many students are studying only one subject.
# Note. It is guaranteed that there are no namesakes among BEEGEEK school students.

# Онлайн-школа BEEGEEK 3
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. У руководителя школы есть списки изучающих каждый предмет.
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m, n = int(input()), int(input())
mat = {input() for _ in range(m)}
inf = {input() for _ in range(n)}

set1 = mat & inf
set2 = len((mat|inf)-set1)
if set2 == 0:
    print('NO')
else:
    print(set2)

Sample Input 1:
5
4
Демин
Рыбаков
Сафонов
Игнатов
Мухин
Сафонов
Игнатов
Демин
Рыбаков
Sample Output 1:
1
Sample Input 2:
3
1
Петухов
Фокин
Самойлов
Фокин
Sample Output 2:
2
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
2
