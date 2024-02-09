# При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# When registering on sites, you are required to enter your password twice. This is done for security purposes, as this approach reduces the possibility of entering the password incorrectly.

# Write a program that compares the password and its confirmation. If they match, then the program displays: “Password accepted,” otherwise: “Password not accepted.”

# Sample Input 2:
# qwerty
# Qwerty
# Sample Output 2:
# Пароль не принят
# Sample Input 3:
# PythonROCKS
# PythonROCKS
# Sample Output 3:
# Пароль принят

a = str(input())
b = str(input())
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')
