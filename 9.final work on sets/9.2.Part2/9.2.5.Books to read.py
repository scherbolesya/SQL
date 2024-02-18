# Books to read
# At the end of the school year, Ruslan received a list of literature for the summer. 
# Now he needs to find out which books from this list he has. Ruslan has all the books from his home library written in a text file on his computer in random order.
# Write a program that determines for each book on the reading list whether Ruslan has it or not.
# Input format
# The input to the program in the first line is a natural number m — the number of books in Ruslan’s home library. 
# The second line contains a natural number n — the number of books on the list for the summer. 
# Next come m lines with titles of books from the home library and n lines of titles from the list for the summer.
# Output format
# The program should print n lines, each of which contains the word YES if the book is found in the library, and NO if it is not.

# Книги на прочтение
# Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. 
# У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
# Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.
# Формат входных данных
# На вход программе в первой строке подается натуральное число m — количество книг в домашней библиотеке Руслана. 
# Во второй строке записано натуральное число n —  количество книг в списке на лето. Далее идут m строк с названиями книг из домашней библиотеки и n строк названий из списка на лето.
# Формат выходных данных
# Программа должна вывести n строк, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.

m,n = int(input()), int(input())
home = {input() for _ in range(m)}
leto = [input() for _ in range(n)]
s = []
for i in range(n):
    if leto[i] in home:
        s.append('YES')
    else:
        s.append('NO')
for c in s:
    print(c)

Sample Input:
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир
Sample Output:
NO
YES
YES
NO
