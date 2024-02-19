# Secret word
# Write a program to decipher a secret word using frequency analysis.
# Note. It is guaranteed that letter frequencies are not repeated.

# Секретное слово
# Напишите программу для расшифровки секретного слова методом частотного анализа.
# Примечание. Гарантируется, что частоты букв не повторяются.

a, b = {}, {}
s = input()
for key in s:
    a[key] = a.get(key, 0) + 1
for _ in range(int(input())):
    key, value = input().split(':')
    b.setdefault(int(value), key)
for i in s:
    print(b[a.get(i)], end='')

Sample Input 1:
*!*!*?
3
а: 3
н: 2
с: 1
Sample Output 1:
ананас
Sample Input 2:
pop
2
д: 2
е: 1
Sample Output 2:
дед
