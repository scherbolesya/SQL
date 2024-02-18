# All 10 digits
# The input to the program is two strings consisting of numbers. 
# It is necessary to determine whether it is true that all ten digits are used in the recording of these two lines?

# Все 10 цифр
# На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?

n = set(input() + input())
print('YES' if len(n) == 10 else 'NO')

# Sample Input 1:
# 12387
# 94230
# Sample Output 1:
# NO
# Sample Input 2:
# 1930
# 2465748
# Sample Output 2:
# YES
# Sample Input 3:
# 12368267374924645234
# 134347264344472183
# Sample Output 3:
# NO
