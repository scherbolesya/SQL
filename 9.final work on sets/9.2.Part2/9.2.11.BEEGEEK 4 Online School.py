# BEEGEEK 4 Online School
# The head of the BEEGEEK online school and his assistant compiled lists of students from their school.
# Write a program that will display all the names of the students that the leader and his assistant remember.
# Note. It is guaranteed that there are no namesakes among BEEGEEK school students.

# Онлайн-школа BEEGEEK 4
# Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.
# Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

set1 = {i for i in input().split()}
set2 = {i for i in input().split()}
print(*sorted(set1|set2))

Sample Input 1:
Блинов Жданов
Бобров Жданов Некрасов Блинов
Sample Output 1:
Блинов Бобров Жданов Некрасов
Sample Input 2:
Рыбаков
Сафонов Игнатов
Sample Output 2:
Игнатов Рыбаков Сафонов
Sample Input 3:
Демин Рыбаков Сафонов Игнатов Мухин
Сафонов Игнатов Демин Рыбаков
Sample Output 3:
Демин Игнатов Мухин Рыбаков Сафонов
