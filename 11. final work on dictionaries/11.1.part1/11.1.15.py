# Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену. 
# Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате username@domain.
# Примечание 1. Для сортировки в алфавитном порядке используйте встроенную функцию sorted(), либо списочный метод sort().
# Примечание 2. Группировать электронные адреса по доменам не нужно.

# The emails dictionary contains information about user email addresses grouped by domain. 
# Modify the code below to display all email addresses in alphabetical order, each on a separate line, in the format username@domain.
# Note 1: To sort alphabetically, use the built-in sorted() function or the sort() list method.
# Note 2: There is no need to group email addresses by domain.

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
a = []
for key, value in emails.items():
    for i in value:
        s = str(i) +'@'+ str(key)
        a.append(s)
for a1 in sorted(a):        
    print(a1)
