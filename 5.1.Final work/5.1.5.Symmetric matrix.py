# Symmetric matrix
# Write a program to check the symmetry of a square matrix with respect to the secondary diagonal.

# Симметричная матрица
# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

n = int(input()) 
matrix = [input().split() for _ in range(n)]
matrix.reverse()
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)

# Sample Input 1:
# 3
# 0 3 10
# 4 9 3
# 7 4 0
# Sample Output 1:
# YES
# Sample Input 2:
# 3
# 0 1 2
# 1 2 7
# 2 3 4
# Sample Output 2:
# NO
# Sample Input 3:
# 2
# 1 2
# 3 4
# Sample Output 3:
# NO
# Sample Input 4:
# 2
# 4 2
# 3 4
# Sample Output 4:
# YES
