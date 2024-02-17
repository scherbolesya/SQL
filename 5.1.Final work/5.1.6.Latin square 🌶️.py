# Latin square 🌶️
# A Latin square of order n is a square matrix of size n×n, each row and each column of which contains all the numbers from 1 to n. 
# Write a program that checks whether a given square matrix is a Latin square.

# Латинский квадрат 🌶️
# Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой содержат все числа от 1 до n. 
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

def provst(n, matrix):
    for i in range(n):
        m = [i for i in range(1,n+1)]
        for j in range(n):
            if matrix[j][i] not in m: return False
            m.remove(m[m.index(matrix[j][i])])
    if m == []: return True
    
    
    
def provs(n, matrix):
    for i in range(n):
        m = [i for i in range(1,n+1)]
        for j in range(n):
            if matrix[i][j] not in m: return False
            m.remove(m[m.index(matrix[i][j])])
    if m == []: return True
    
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

if provs(n, matrix) == False: print('NO')
else: 
    if provst(n, matrix) == False: print('NO')
    else: print('YES')

# Sample Input 1:
# 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# Sample Output 1:
# YES
# Sample Input 2:
# 3
# 1 2 3
# 3 2 1
# 2 3 4
# Sample Output 2:
# NO
