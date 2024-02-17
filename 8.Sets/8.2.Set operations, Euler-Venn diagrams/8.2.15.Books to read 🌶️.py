# Books to read 🌶️
# 10th grade students of the BEEGEEK online school were assigned to read three books during the summer holidays:
# "What is mathematics?";
# "Mathematical component";
# "100 brilliant ideas for mathematics."
# It turned out that n students read the first book, m students read the second, k students read the third. 
# It is also known that x students read the first or second, or both of these books, y students read the second or third, or both, 
# z students read the first and third, or at least one of these two books. Only t students completed the task completely. 
# There are a total of a students in the 10th grade. Write a program that prints how many students there are:
# read only one book;
# read two books;
# Haven't read any of the recommended books.

# Книги на прочтение 🌶️
# Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:
# "Что такое математика?";
# "Математическая составляющая";
# "100 гениальных идей по математике".
# Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. 
# Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, 
# или обе, z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников. 
# Всего в 10 классе учится a учеников. Напишите программу, которая выводит сколько учеников:
# прочитали только одну книгу;
# прочитали две книги;
# не прочитали ни одной из рекомендованных книг.

n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
b1=(n+m-t)-x
b2=(m+k-t)-y
b3=(k+n-t)-z
b=b1+b2+b3#2book

k1=k-b3-t-b2
n1=n-b1-b3-t
m1=m-b1-t-b2
o=k1+n1+m1#1book

d=a-b-o-t

print(o)
print(b)
print(d)

# Sample Input:
# 19
# 18
# 22
# 32
# 33
# 35
# 2
# 50
# Sample Output:
# 29
# 12
# 7
