# Total numbers
# The program receives two lines of text containing numbers as input. 
# Write a program that prints all the numbers in ascending order that appear in both the first line and the second.

# Общие числа
# На вход программе подаются две строки текста, содержащие числа. 
# Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

n,m = input().split(), input().split()
a, b = set(), set()
for i in n:
    a.add(int(i))
for j in m:
    b.add(int(j))
s = a & b
print(*sorted(s))

Sample Input 1:
1 2 3
1 2 4 5
Sample Output 1:
1 2
Sample Input 2:
1 3 5
5 3 1
Sample Output 2:
1 3 5
Sample Input 3:
1 7 8 9 7 3
6 4 3 2 7 3 10 5
Sample Output 3:
3 7
