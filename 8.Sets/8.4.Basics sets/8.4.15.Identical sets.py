# Identical sets
# The input to the program is two strings consisting of numbers. 
# It is necessary to determine whether it is true that the same sets of numbers were used to write these lines?

# Одинаковые наборы
# На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, 
# что для записи этих строк были использованы одинаковые наборы цифр?

print('YES' if set(input()) == set(input()) else 'NO')

# Sample Input 1:
# 0943
# 9304
# Sample Output 1:
# YES
# Sample Input 2:
# 1
# 2
# Sample Output 2:
# NO
# Sample Input 3:
# 327428
# 824723
# Sample Output 3:
# YES
