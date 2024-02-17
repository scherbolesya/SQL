# Programmer Timur wrote a program for working with biographical data of Russian poets. 
# The data is contained in tuples of the form (last name, year of birth, city of birth). 
# While the program was running, an error was detected in some poet_data tuple: ('Pushkin', 1799, 'St. Petersburg'). 
# The place of birth is incorrectly indicated here, because Alexander Pushkin was born in Moscow.
# Complete the code below so that the poet_data variable contains the correct tuple (with the corrected value), and then print its contents.

# Программист Тимур написал программу для работы с биографическими данными русских поэтов. 
# Данные содержатся в кортежах вида (фамилия, год рождения, город рождения). 
# В процессе работы программы в некотором кортеже poet_data обнаружилась ошибка: ('Пушкин', 1799, 'Санкт-Петербург'). 
# Тут неверно указано место рождения, ведь Александр Пушкин родился в Москве.
# Дополните приведенный код так, чтобы в переменной poet_data находился правильный кортеж (с исправленным значением), а затем выведите его содержимое.

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
a = list(poet_data)
a[2] = 'Москва'
poet_data = tuple(a)
print(poet_data)
