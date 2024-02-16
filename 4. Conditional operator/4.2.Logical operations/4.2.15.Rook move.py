# Rook move
# Given two different squares of a chessboard. Write a program that determines
# can a rook get from the first square to the second in one move. The program receives four numbers from 1 to 8 each as input,
# specifying the column number and row number first for the first cell, then for the second cell. The program should output "YES"
# if you can move the rook from the first square to the second, or “NO” otherwise.

# Ход ладьи
# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
# может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.

a = int(input())  #кординаты ладьи 
b = int(input())
a1 = int(input())
b1 = int(input())
if a != a1 and b == b1 or b != b1 and a == a1:
    print('YES')
else:
    print('NO')


# Sample Input 1:
# 4
# 4
# 5
# 4
# Sample Output 1:
# YES
# Sample Input 2:
# 4
# 4
# 5
# 5
# Sample Output 2:
# NO
# Sample Input 3:
# 4
# 4
# 4
# 5
# Sample Output 3:
# YES
