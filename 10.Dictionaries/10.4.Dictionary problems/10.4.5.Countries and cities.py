# Countries and cities
# The program receives a list of countries and cities in each country as input. Then the names of the cities are given. Write a program that for each city displays what country it is in.

# Страны и города
# На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.

result = {}
for i in range(int(input())):
    s = input().split()
    for j in range(1,len(s)):
        result[s[j]] = s[0]
for i in range(int(input())):
    print(result.get(input()))

Sample Input:
2
Германия Берлин Мюнхен Гамбург Дортмунд
Нидерланды Амстердам Гаага Роттердам Алкмар
4
Амстердам
Алкмар
Гамбург
Гаага
Sample Output:
Нидерланды
Нидерланды
Германия
Нидерланды
