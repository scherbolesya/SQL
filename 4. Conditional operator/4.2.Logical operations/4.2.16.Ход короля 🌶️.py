# Ход короля 🌶️
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, 
# может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.

# King's move 🌶️
# Given two different squares of a chessboard. Write a program that determines whether the king can get from the first square to the second in one move. 
# The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, 
# then for the second cell. The program should output “YES” if the king can move from the first cell to the second, or “NO” otherwise.

a = int(input())  #может ли король попасть на след клетку с шагом 1 по прямой и горизонтали
b = int(input())
a1 = int(input())
b1 = int(input())
if -1 <= a - a1 <= 1 and -1 <= b - b1 <= 1:
    print('YES')
else:
    print('NO')
  
# Sample Input 1:
# 4
# 4
# 5
# 5
# Sample Output 1:
# YES
# Sample Input 2:
# 4
# 4
# 5
# 4
# Sample Output 2:
# YES
# Sample Input 3:
# 4
# 4
# 2
# 4
# Sample Output 3:
# NO
