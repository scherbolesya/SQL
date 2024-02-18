# General figures
# The input to the program is a natural number n, and then n different natural numbers, each on a separate line. 
# Write a program that prints all the common digits in ascending order for all entered numbers.

# Общие цифры
# На вход программе подается натуральное число 
# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

a = set('0123456789')
for i in range(int(input())):
    a &= set(input())
if a != set():
    print(*sorted(a))

Sample Input 1:
4
12345
236
3452222
9302
Sample Output 1:
2 3
Sample Input 2:
6
1234567890
87654321
34567890
987234356
1236789
987532
Sample Output 2:
3 7 8
Sample Input 3:
3
4545436
345345
76857
Sample Output 3:
5
