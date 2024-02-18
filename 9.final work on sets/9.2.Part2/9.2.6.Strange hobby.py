# Strange hobby
# As you know, mathematicians are strange people. Timur, the author of this course, is no exception. 
# Every day Timur solves exactly two complex mathematical problems. When solving the first problem, 
# he writes down on the first piece of paper all the numbers that appear in it. Then he pauses and takes on the second task. 
# Then he writes down on the second piece of paper all the numbers that appear in it. After that, he takes another piece of 
# paper and writes down on it all the matching numbers from the first two pieces of paper. If there are such numbers, the day is a success; 
# if there are no general numbers, Timur considers the day unsuccessful.
# Write a program that finds the common numbers of two leaves or reports that the day was not a success 😏.

# Странное увлечение
# Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. 
# Каждый день Тимур решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все числа, 
# которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором листочке все числа, 
# которые в ней встречаются. После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков. 
# Если такие числа есть — день удался, если общих чисел нет — Тимур считает день неудачным.
# Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏.

set1 = {int(c) for c in input().split()}
set2 = {int(c) for c in input().split()}
print(*sorted(set1.intersection(set2), reverse=True) if len(set1.intersection(set2)) > 0 else ('BAD DAY',))

Sample Input 1:
6 56 7 34 14
675 45 246 2 1
Sample Output 1:
BAD DAY
Sample Input 2:
1 2 3 4 5 6 12
6 5 4 3 2 1
Sample Output 2:
6 5 4 3 2 1
Sample Input 3:
24 6 14 7
7 24 6 98 53
Sample Output 3:
24 7 6
