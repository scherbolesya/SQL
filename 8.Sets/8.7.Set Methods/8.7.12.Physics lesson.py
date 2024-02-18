# Physics lesson
# The physics scores of three students are given on a 10-point scale. 
# Write a program that prints the set of grades for the third student that are not found in either the first or the second student.
# Note. A student's score ranges from 0 to 10 inclusive.

# Урок физики
# Даны по 10-балльной шкале оценки по физике трех учеников. 
# Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

set1, set2, set3 = [set(int(i) for i in input().split()) for _ in range(3)] 
print(*sorted((set3 - set2 - set1), reverse = True))

Sample Input 1:
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:
10 9 8 0
Sample Input 2:
2 9 2 4 6 10
2 2 4 5 2 10
2 3 4 5 3 9
Sample Output 2:
3
Sample Input 3:
3 4 5 6 2 10 3 9 8 8 4
5 7 8 9 2 7 4 6 8 2 5
2 6 7 1 3 6 5 9 2 6 10
Sample Output 3:
1
