# Unique characters 2
# Write a program to display the total number of unique characters in all words read, case insensitive.
# Уникальные символы 2
# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

a = ''
for i in range(int(input())):
    a = a + input().lower()
print(len(set(a)))

# Sample Input 1:
# 5
# aAa
# bB
# ccc
# dDdd
# ppppP
# Sample Output 1:
# 5
# Sample Input 2:
# 4
# авТорИтет
# небо
# машинА
# Мёд
# Sample Output 2:
# 13
# Sample Input 3:
# 4
# троС
# рОст
# сорт
# тОрС
# Sample Output 3:
# 4
