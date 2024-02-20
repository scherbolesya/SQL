# Напишите программу, которая с помощью модуля random генерирует случайный пароль. 
# Программа принимает на вход длину пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
# Примечание 1. Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
# Примечание 2. Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.
# Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.
# Примечание 4. Например, при длине пароля, равной 15 символам, ваша программа может выводить:

# Write a program that uses the random module to generate a random password.
# The program takes the password length as input and outputs a random password containing only the English alphabet characters a..z, A..Z (lower and upper case).
# Note 1. The English characters A..Z correspond to numbers 65 to 90 in the ASCII character table.
# Note 2: The English a..z characters correspond to numbers 97 to 122 in the ASCII character table.
# Note 3: Use the chr() function to get a character by its number in the ASCII character table.
# Note 4: For example, with a password length of 15 characters, your program might output:

peJFAmhqfaAeKDu

import random
for _ in range(int(input())):
    a = random.randint(97,122)
    b = random.randint(0,1)
    if b == 1:
        print(chr(a).upper(), end='')
    else:
        print(chr(a), end='')
