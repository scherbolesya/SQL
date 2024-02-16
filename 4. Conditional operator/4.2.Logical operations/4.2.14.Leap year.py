# Leap year
# A year is a leap year if its number is a multiple of 4 but not a multiple of 100, or if it is a multiple of 400.
# Високосный год
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('YES')
else:
    print('NO')
  
# Sample Input 1:
# 2020
# Sample Output 1:
# YES
# Sample Input 2:
# 2012
# Sample Output 2:
# YES
# Sample Input 3:
# 2009
# Sample Output 3:
# NO
