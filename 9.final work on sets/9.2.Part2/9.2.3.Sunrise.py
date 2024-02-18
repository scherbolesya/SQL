# Sunrise
# The Voskhod satellite has an instrument for measuring solar activity. 
# Every minute it transmits to the observatory via a communication channel a positive integer - the amount of solar radiation energy. 
# To properly analyze the results, there is no need to keep duplicate data, so they need to be removed. 
# Write a program that prints the maximum number of satellite readings that, if removed, will correctly analyze the result.
# Input format
# The input to the program is one line containing numbers - readings from the Voskhod satellite. Numbers are separated by spaces and do not contain leading zeros.
# Output format
# The program should display the maximum number of readings, after removing which the results will be analyzed correctly.
# Note. Let's consider test 1: we have data 10 20 30 10 40 10. We see that the number 10 is contained here 3 times - which means that duplicate numbers 10 must be removed. We have 2 of these (we do not take into account the first number 10). The other numbers are not repeated, so the answer is 2.

# Восход
# На спутнике «Восход» установлен прибор для измерения солнечной активности. 
# Каждую минуту он передаёт в обсерваторию по каналу связи положительное целое число — количество энергии солнечного излучения. 
# Для правильного анализа результатов нет необходимости держать повторяющиеся данные, поэтому их нужно удалить. 
# Напишите программу, которая выводит максимальное количество показаний спутника, при удалении которых результат будет правильно проанализирован.
# Формат входных данных
# На вход программе подаётся одна строка, содержащая числа – показания спутника «Восход». Числа указываются через пробел и не содержат ведущих нулей.
# Формат выходных данных
# Программа должна вывести максимальное количество показаний, после удаления которых анализ результатов будет произведен верно.
# Примечание. Рассмотрим 1 тест: у нас подаются данные 10 20 30 10 40 10. Мы видим, что число 10 содержится тут 3 раза – значит, повторяющиеся числа 10 надо удалить. 
# Таких у нас 2 (первое число 10 мы не учитываем). Другие числа не повторяются, поэтому ответ будет 2.

s = input().split()
set1 = set(s)
print(len(s)-len(set1))

Sample Input 1:
10 20 30 10 40 10
Sample Output 1:
2
Sample Input 2:
1 2 3 4 5 6 7 8 9 1 2 3
Sample Output 2:
3
Sample Input 3:
100 100 100 100 100 100 100
Sample Output 3:
6
