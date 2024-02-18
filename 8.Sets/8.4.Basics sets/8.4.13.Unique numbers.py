# Unique numbers
# The input to the program is a string consisting of numbers. 
# It is necessary to determine whether it is true that none of the numbers are repeated in its recording?

# Неповторимые цифры
# На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?

n = input()
a = len(n)
n1 = len(set(n))
if a == n1:
    print('YES')
else:
    print('NO')

# Sample Input 1:
# 1093482
# Sample Output 1:
# YES
# Sample Input 2:
# 10000000
# Sample Output 2:
# NO
# Sample Input 3:
# 3445321290
# Sample Output 3:
# NO
