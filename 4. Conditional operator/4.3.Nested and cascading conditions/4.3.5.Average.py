# Average
# Three different integers are given. Write a program that finds the average of a number.
  
# Среднее число
# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input()) # из 3х чисел ищет среднее число
if a<b<c or c<b<a:
    print(b)
elif b<a<c or c<a<b:
    print(a)
elif b<c<a or a<c<b:
    print(c)
  
# Sample Input 1:
# 1
# 2
# 3
# Sample Output 1:
# 2
# Sample Input 2:
# 10
# 30
# 20
# Sample Output 2:
# 20
# Sample Input 3:
# 67
# 100
# 54
# Sample Output 3:
# 67
# Sample Input 4:
# 54
# 34
# 33
# Sample Output 4:
# 34
