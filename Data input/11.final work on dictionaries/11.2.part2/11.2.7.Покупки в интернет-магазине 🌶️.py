# Покупки в интернет-магазине 🌶️
# Покупки в интернет-магазине 🌶️

# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.
# Write a program to count the number of units of each type of product purchased by each customer in an online store.

# Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список 
# попадает суммарное количество товара по данной позиции.
# Note. Pay attention to the second test. If items of goods are repeated, then the total quantity of goods for this item is included in the final list.

s = {}
for _ in range(int(input())):
    key, key1, count = input().split()
    s[key] = s.get(key, {})
    s[key][key1] = s[key].get(key1, 0) + int(count)
for key in sorted(s.keys()):
    print(f'{key}:')
    for key1, count in sorted(s[key].items()):
        print(key1, count)

Sample Input 1:
5
Руслан Пирог 1
Тимур Карандаш 5
Руслан Линейка 2
Тимур Тетрадь 12
Руслан Хлеб 3
Sample Output 1:
Руслан:
Линейка 2
Пирог 1
Хлеб 3
Тимур:
Карандаш 5
Тетрадь 12
Sample Input 2:
7
Вячеслав Ручка 1
Филипп Ручка 1
Виктория Перо 3
Вячеслав Линейка 4
Виктория Тетрадь 7
Вячеслав Ручка 29
Филипп Циркуль 1
Sample Output 2:
Виктория:
Перо 3
Тетрадь 7
Вячеслав:
Линейка 4
Ручка 30
Филипп:
Ручка 1
Циркуль 1
Sample Input 3:
5
Максим Пирог 5
Максим Печенье 55
Максим Свеча 3
Максим Тарелки 10
Максим Торт 1
Sample Output 3:
Максим:
Печенье 55
Пирог 5
Свеча 3
Тарелки 10
Торт 1
