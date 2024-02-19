# Phone book
# Timur wrote down the phone numbers of all his friends to automate the search for the right number.
# Each of Timur's friends may have one or more phone numbers. Write a program that will help Timur find all the numbers of a certain friend.
# Note 1. Print the telephone numbers of one person on one line separated by a space in the order in which they were specified in the input data.
# Note 2. The number of lines in the answer must be equal to the number m.
# Note 3. A phone number is several numbers written in a row, and a name can consist of letters of the Russian or English alphabet. Entries are not repeated.

# Телефонная книга
# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга.
# Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.
# Примечание 2. Количество строк в ответе должно быть равно числу m.
# Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита. Записи не повторяются.

result = {}
for _ in range(int(input())):
    value, key = input().lower().split()
    result[key] = result.get(key, []) + [value]
for _ in range(int(input())):
    key = input().lower()
    s = result.get(key, ['абонент не найден'])
    print(*s)

Sample Input:
3
79184219577 Женя
79194249271 Руслан
79281234567 Женя
3
Руслан
женя
Рустам
Sample Output:
79194249271
79184219577 79281234567
абонент не найден
