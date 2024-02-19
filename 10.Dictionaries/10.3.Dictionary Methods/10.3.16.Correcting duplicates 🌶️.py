# Correcting duplicates 🌶️
# The input to the program is a string containing identifier strings. Write a program that corrects them so that there are no duplicates in the resulting string. 
# To do this, it is necessary to add the postfix _n to repeating identifiers, where n is the number of times such an identifier has already been encountered.

# Исправление дубликатов 🌶️
# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. 
# Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

result = {}
for num in input().split():
    result[num] = result.get(num, -1) + 1
    if result[num]==0:
        print(num, end=' ')
    else:
        print(f'{num}_{result[num]}', end=' ')

Sample Input 1:
a b c a a d c
Sample Output 1:
a b c a_1 a_2 d c_1
Sample Input 2:
a b c
Sample Output 2:
a b c
Sample Input 3:
i am i r o n m a n
Sample Output 3:
i am i_1 r o n m a n_1
Sample Input 4:
a a a a a
Sample Output 4:
a a_1 a_2 a_3 a_4
