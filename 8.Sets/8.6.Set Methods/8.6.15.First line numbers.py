# First line numbers
# The program receives two lines of text containing numbers as input. 
# Write a program that prints all the numbers in ascending order that are in the first line but not in the second.

# Числа первой строки
# На вход программе подаются две строки текста, содержащие числа. 
# Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
print(*sorted(set1 - set2))

Sample Input 1:
1 2 3 4
5 6 7 8
Sample Output 1:
1 2 3 4
Sample Input 2:
1 2 3 4 5
1 2 3 4 6
Sample Output 2:
5
