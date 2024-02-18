# Information about training courses
# Write a program that displays information about a given course based on the course number.
# Информация об учебных курсах
# Напишите программу, которая по номеру курса выводит информацию о данном курсе.
Номер курса (ключ)	Номер аудитории (значение)	Преподаватель (значение)	Время (значение)
CS101	              3004	                      Хайнс	                    8:00
CS102	              4501	                      Альварадо	                9:00
CS103	              6755	                      Рич	                     10:00
NT110	              1244	                      Берк	                   11:00
CM241              	1411	                      Ли	                     13:00


# Примечание 1. Используйте словарь вместо условного оператора.
# Примечание 2. Для удобного вывода используйте строковый метод format() или f-строки.

# Note 1: Use a dictionary instead of a conditional statement.
# Note 2: For convenient output, use string method format() or f-strings.

d = {
    "CS101": "3004, Хайнс, 8:00",
    "CS102": "4501, Альварадо, 9:00",
    "CS103": "6755, Рич, 10:00",
    "NT110": "1244, Берк, 11:00",
    "CM241": "1411, Ли, 13:00"
}
a = input()
print(f'{a}: {d[a]}')

Sample Input 1:
CS101
Sample Output 1:
CS101: 3004, Хайнс, 8:00
Sample Input 2:
CM241
Sample Output 2:
CM241: 1411, Ли, 13:00
Sample Input 3:
CS102
Sample Output 3:
CS102: 4501, Альварадо, 9:00
