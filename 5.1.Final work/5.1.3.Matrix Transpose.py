# Matrix Transpose
# Write a program that transposes a square matrix.
# Note 1. Transposed matrix is a matrix obtained from the original matrix by replacing rows with columns.

# Транспонирование матрицы
# Напишите программу, которая транспонирует квадратную матрицу.
# Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)] 
for c in range(n):                    #меняем местами строки со столбцами
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()

# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 1 4 7
# 2 5 8
# 3 6 9
# Sample Input 2:
# 4
# 1 2 3 1
# 4 5 6 4
# 7 8 9 7
# 1 2 3 8
# Sample Output 2:
# 1 4 7 1
# 2 5 8 2
# 3 6 9 3
# 1 4 7 8
# Sample Input 3:
# 2
# 5 6
# 8 4
# Sample Output 3:
# 5 8
# 6 4

