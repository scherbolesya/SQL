# Programmer's Dictionary
# Programmers, as you already know, are constantly learning, and when communicating with each other they use a very specific language. 
# To help organize your growing professional vocabulary, we came up with this challenge. 
# Write a program to create a small dictionary of slang programming expressions so that it can then return values from this dictionary upon request.

# Note 1. A mini-dictionary for beginning developers can be found here.
# Note 2: It is guaranteed that the word or phrase being defined does not contain a colon (:) followed by a space.

# Словарь программиста
# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. 
# Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. 
# Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

# Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.
# Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.

result = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    result[key.lower()] = value
for _ in range(int(input())):
    print(result.get(input().lower(), 'Не найдено'))

Sample Input 1:
5
Змея: язык программирования Python
Баг: от англ. bug — жучок, клоп, ошибка в программе
Конфа: конференция
Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
Бета: бета-версия, приложение на стадии публичного тестирования
3
Змея
Жаба
костыль
Sample Output 1:
язык программирования Python
Не найдено
код, который нужен, чтобы исправить несовершенство ранее написанного кода
Sample Input 2:
7
Бэкенд: программно-аппаратная или серверная часть приложения
Бэкап: резервная копия или процесс создания резервной копии приложения
Галера: компания, в которой платят низкие зарплаты и не ценят разработчиков
Гит: система контроля версий Git или сервис GitHub
Г***окод: плохой, некачественный код
Жаба: язык программирования Java
Жабаскрипт: язык программирования JavaScript
6
Жаба
Змея
Костыль
Бета
БЭКЕНД
Г***окод
Sample Output 2:
язык программирования Java
Не найдено
Не найдено
Не найдено
программно-аппаратная или серверная часть приложения
плохой, некачественный код
