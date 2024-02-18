# BEEGEEK 5 Online School 🌶️
# Every student studying at the BEEGEEK online school studies either mathematics or computer science, or both of these subjects. 
# The head of the school has lists of students studying each subject. By chance, the lists of all the students got mixed up.
# Write a program that allows a teacher to find out how many students are studying only one subject.
# Note. It is guaranteed that there are no namesakes among BEEGEEK school students.

# Онлайн-школа BEEGEEK 5 🌶️
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. 
# У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m,n = int(input()), int(input())
mat = set()
inf = set()
for i in range(m+n):
    s = input()
    if len(mat) != m:
        if s not in mat:
            mat.add(s)
        else:
            inf.add(s)
    else:
        if s not in inf:
            inf.add(s)
a = mat.difference(inf) | inf.difference(mat) 
if len(a) == 0:
    print('NO')
else:
    print(len(a))

Sample Input 1:
2
3
Хохлов
Фадеев
Ершов
Ушаков
Хохлов
Sample Output 1:
3
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
6
