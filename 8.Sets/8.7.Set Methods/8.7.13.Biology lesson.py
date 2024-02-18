# Biology lesson
# Given on a 10-point scale for biology assessments for three students. 
# Write a program that prints the set of scores that are not found in any of the three students.
# Note. A student's score ranges from 0 to 10 inclusive.

# Урок биологии
# Даны по 10-балльной шкале оценки по биологии трех учеников. 
# Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

s = {0,1,2,3,4,5,6,7,8,9,10}
set1, set2, set3 = [set(int(i) for i in input().split()) for _ in range(3)] 
print(*sorted(s - set3 - set2 - set1))

Sample Input 1:
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 8 8 7 0 6 0 3 8 1
Sample Output 1:
9 10
Sample Input 2:
2 9 3 4 6 10
2 3 4 5 2 10
2 3 4 5 3 9
Sample Output 2:
0 1 7 8
Sample Input 3:
3 4 5 6 4 1 3 9 8 8
5 7 8 9 3 7 4 6 8 4
1 6 7 1 3 6 5 9 7 6
Sample Output 3:
0 2 10
