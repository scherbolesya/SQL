# Maximum in area 2
# Write a program that prints the maximum element in the shaded region of a square matrix.

# Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
m = matrix[0][0] 
for i in range(n):
    for j in range(n):
        if (i >= j and i >= (n-j-1)) or (i<=j and i >= (n-j-1)):
            if m < matrix[i][j]:
                m = matrix[i][j]
print(m)

# Sample Input 1:
# 3
# 1 4 5
# 6 7 8
# 1 1 6
# Sample Output 1:
# 8
# Sample Input 2:
# 4
# 0 1 4 6
# 0 0 2 5
# 0 0 0 7
# 0 0 0 0
# Sample Output 2:
# 7
# Sample Input 3:
# 2
# 6 0
# 7 9
# Sample Output 3:
# 9
