# Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество попыток и выводит результаты бросков: 
# Орел или Решка (каждое на отдельной строке).
# Примечание. Например, при n=7 ваша программа может выводить:

# Write a program that uses the random module to simulate coin tosses. The program takes as input the number of attempts and displays the results of the throws:
# Heads or Tails (each on a separate line).
# Note. For example, with n=7 your program might output:
Орел
Решка
Решка
Орел
Орел
Орел
Решка

import random
for _ in range(int(input())):
    a = random.randint(0, 1)
    print('Решка' if a == 1 else 'Орел')
