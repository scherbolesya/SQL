# Unique characters 1
# Write a program to display the number of unique characters of each word read, case insensitive.
# Уникальные символы 1
# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

a = []
for i in range(int(input())):
    a.append(len(set(input().lower())))
for j in a:
    print(j)

# Sample Input 1:
# 3
# Тимур
# Beegeek
# АнанАс
# Sample Output 1:
# 5
# 4
# 3
# Sample Input 2:
# 5
# абОнемЕнТы
# дозировка
# военкОмат
# ДрУжиНник
# ОпПозицИя
# Sample Output 2:
# 8
# 8
# 8
# 7
# 6
# Sample Input 3:
# 2
# прЕвыСокОмнОгОраСсмотРИтельствУюЩиЙ
# вОдоГрязетоРфопарАфинОлечЕние
# Sample Output 3:
# 20
# 16
