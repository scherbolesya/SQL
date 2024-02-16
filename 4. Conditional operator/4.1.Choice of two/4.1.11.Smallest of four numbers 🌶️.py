# Smallest of four numbers 🌶️
# Наименьшее из четырёх чисел 🌶️
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b :
    counter = b
else:
    counter = a
if c > d:
    counter2 = d
else:
    counter2 = c
if counter > counter2:
    print(counter2)
else:
    print(counter)
# Sample Input 1:
# 1
# 2
# 3
# 4
# Sample Output 1:
# 1
# Sample Input 2:
# 10
# 9
# 11
# 12
# Sample Output 2:
# 9
# Sample Input 3:
# 100
# 200
# 5
# 300
# Sample Output 3:
# 5
