# Diagonals parallel to the main one
# The program input is a natural number n. Write a program that creates an n×n matrix and fills it according to the following rule:
# - on the main diagonal there should be a number 0 in place of each element;
# - on two diagonals adjacent to the main one - the number 1;
# - on the next two diagonals - the number 2, etc.

# Диагонали, параллельные главной
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:
# - на главной диагонали на месте каждого элемента должно стоять число 0;
# - на двух диагоналях, прилегающих к главной, – число 1;
# - на следующих двух диагоналях – число 2, и т.д.

n = int(input())
matrix=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j]=abs(i-j)
for a in matrix:
    print(*a)

# Sample Input 1:
# 5
# Sample Output 1:
# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0
# Sample Input 2:
# 2
# Sample Output 2:
# 0 1
# 1 0
# Sample Input 3:
# 3
# Sample Output 3:
# 0 1 2
# 1 0 1
# 2 1 0
