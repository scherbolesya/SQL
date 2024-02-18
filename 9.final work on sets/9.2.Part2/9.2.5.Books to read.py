# Books to read
# At the end of the school year, Ruslan received a list of literature for the summer. 
# Now he needs to find out which books from this list he has. Ruslan has all the books from his home library written in a text file on his computer in random order.
# Write a program that determines for each book on the reading list whether Ruslan has it or not.

# Книги на прочтение
# Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. 
# У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
# Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

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
