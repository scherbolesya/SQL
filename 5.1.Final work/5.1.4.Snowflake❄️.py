# Snowflake ❄️
# An odd natural number n is given as input to the program.
# Write a program that creates a matrix of size n×n filling it with symbols. 
# Then fill in the middle row and column of the matrix, the main and secondary diagonals of 
# the matrix with * symbols. Display the resulting matrix on the screen, separating elements with spaces.

# Снежинка ❄️
# На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её символами. 
# Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

n = int(input())
matrix = [['.']*n for _ in range(n)] 
for i in range(n): 
    matrix[i][i] = '*' #главная диагональ
    matrix[i][~i] = '*' #побочная диагональ
    matrix[i][n//2] = '*'
    matrix[n//2][i] = '*'
for row in matrix:
    print(*row)

Sample Input 1:
5
Sample Output 1:
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *

Sample Input 2:
7
Sample Output 2:
* . . * . . *
. * . * . * .
. . * * * . .
* * * * * * *
. . * * * . .
. * . * . * .
* . . * . . *

Sample Input 3:
11
Sample Output 3:
* . . . . * . . . . *
. * . . . * . . . * .
. . * . . * . . * . .
. . . * . * . * . . .
. . . . * * * . . . .
* * * * * * * * * * *
. . . . * * * . . . .
. . . * . * . * . . .
. . * . . * . . * . .
. * . . . * . . . * .
* . . . . * . . . . *
