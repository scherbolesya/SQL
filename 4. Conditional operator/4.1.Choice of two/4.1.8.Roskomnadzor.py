# Roskomnadzor
# Write a program that determines whether a user is allowed to access an Internet resource or not.
# Output format
# The program should display the text “Access allowed” if the age is at least 18, and “Access denied” otherwise.
  
# Роскомнадзор
# Напишите программу, которая определяет, разрешен ли пользователю доступ к интернет-ресурсу или нет.
# Формат выходных данных
# Программа должна вывести текст «Доступ разрешен», если возраст не менее 18, и «Доступ запрещен» - в противном случае.

age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')


# Sample Input 1:
# 16
# Sample Output 1:
# Доступ запрещен
# Sample Input 2:
# 18
# Sample Output 2:
# Доступ разрешен
# Sample Input 3:
# 19
# Sample Output 3:
# Доступ разрешен
