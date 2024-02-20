# Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями. 
# Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика (каждое на отдельной строке).
# Примечание. Например, при n=7 ваша программа может выводить:
# Write a program that uses the random module to simulate the rolls of a 6-sided die.
# The program takes as input the number of attempts and displays the results of the throws - the dropped number, which is written on the face of the cube (each on a separate line).
# Note. For example, with n=7 your program might output:
5
5
6
6
2
6
2

import random
for _ in range(int(input())):
    print(random.randint(1,6))
