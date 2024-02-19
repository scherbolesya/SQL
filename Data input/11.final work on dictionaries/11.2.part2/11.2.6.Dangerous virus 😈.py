# Dangerous virus 😈
# Опасный вирус 😈

В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль прав доступа к файлам. 
Говорят, вирус написал один из студентов курса Python для начинающих.
Для каждого файла известно, с какими действиями можно к нему обращаться:
запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам. 
Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

A dangerous virus penetrated the file system of the computer on which our ❤️ Stepik platform is deployed and broke the control of access rights to files. 
They say that the virus was written by one of the students of the Python course for beginners.
For each file it is known what actions can be performed on it:
write W (write, access to write to a file);
read R (read, access to read from file);
launch X (execute, launch to execute a file).
Write a program to restore access control to files. 
Your program for each request will need to return OK if a valid operation is performed, and Access denied if the operation is invalid.

a = {}
s = {'write': 'W', 'read': 'R','execute': 'X'}
for _ in range(int(input())):
    key, *value = input().split()
    a[key] = value
for _ in range(int(input())):
    f, f1 = input().split()
    if s[f] in a[f1]:
        print('OK')
    else:
        print('Access denied')

Sample Input 1:
5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe
Sample Output 1:
Access denied
Access denied
OK
OK
OK
OK
Sample Input 2:
2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com
Sample Output 2:
OK
Access denied
