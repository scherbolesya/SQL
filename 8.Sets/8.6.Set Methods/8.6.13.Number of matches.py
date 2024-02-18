# Number of matches
# The program receives two lines of text containing numbers as input. 
# Write a program that determines the number of numbers that are in both the first line and the second.

# Количество совпадающих
# На вход программе подаются две строки текста, содержащие числа. 
# Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.

n,m = set(input().split()), set(input().split())
set3 = n.intersection(m)
print(len(set3))

Sample Input 1:
1 3 2
4 3 2
Sample Output 1:
2
Sample Input 2:
1 2 6 4 5 7
10 2 3 4 8
Sample Output 2:
2
Sample Input 3:
1 7 3 8 10 2 5
6 5 2 8 4 3 7
Sample Output 3:
5
