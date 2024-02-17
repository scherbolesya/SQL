# Tribonacci sequence
# Write a program that reads a natural number n and prints the first n numbers of the Tribonacci sequence.

# Последовательность Трибоначчи
# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Трибоначчи.

n = int(input()) 
f1, f2, f3 = 1, 1, 1
s = []
for i in range(n):
    if i<=2: s.append(f3)
    if i>2:
        f1, f2, f3 = f2, f3, f1 + f2 + f3
        s.append(f3)
print(*s)

# Sample Input 1:
# 10
# Sample Output 1:
# 1 1 1 3 5 9 17 31 57 105
# Sample Input 2:
# 1
# Sample Output 2:
# 1
# Sample Input 3:
# 2
# Sample Output 3:
# 1 1
