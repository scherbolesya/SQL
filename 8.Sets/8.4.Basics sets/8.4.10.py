# Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.
# Complete the code below to print the sum of the squares of the elements of the set numbers.
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
s = 0
for n in numbers:
    s = s + n*n
print(s)
