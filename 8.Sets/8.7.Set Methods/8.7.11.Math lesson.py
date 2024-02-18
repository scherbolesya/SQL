# Math lesson
# Mathematics scores for three students are given on a 10-point scale. 
# Write a program that prints the scores that occur in no more than two students.
# Note. A student's score ranges from 0 to 10 inclusive.

# Урок математики
# Даны оценки по математике трёх учеников в 10-балльной шкале. 
# Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

set1, set2, set3 = [set(int(i) for i in input().split()) for _ in range(3)] 
set4 = set1 & set2 & set3             #Возвращает множество, являющееся пересечением множеств
set5 = set().union(set1, set2, set3)  # объединяем
print(*sorted(set5 - set4))           # находим разность

Sample Input 1:
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 10 2 10 2 6 7 10 10 6
1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:
0 1 2 3 4 5 7 8 9 10
Sample Input 2:
2 9 3 4 6 9
2 3 4 5 2 10
2 3 4 5 3 10
Sample Output 2:
5 6 9 10
Sample Input 3:
3 4 5 6 2 10 3 9 8 8
5 7 8 9 2 7 4 6 8 2
2 6 7 1 3 6 5 9 2 6
Sample Output 3:
1 3 4 7 8 10
