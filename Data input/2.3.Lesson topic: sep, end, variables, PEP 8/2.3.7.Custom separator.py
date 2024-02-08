# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.
# Write a program that reads a delimiter line and three lines, and then outputs the specified lines through the delimiter.

# Sample Input 3:
# python
# 1
# 2
# 3
# Sample Output 3:
# 1python2python3

name1 = input()
name2 = input()
name3 = input()
name4 = input()
print(name2, name3, name4, sep=name1) # 1python2python3
