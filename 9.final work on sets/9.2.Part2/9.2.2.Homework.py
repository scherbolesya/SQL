# Homework
# The teacher checks homework in class and received the following answers: out of n schoolchildren, 
# m had their homework eaten by a dog, k had their lights turned off, and p students suffered both misfortunes. 
# Write a program that determines how many people have completed their homework.

# Домашнее задание
# Учитель проверяет домашнее задание в классе и получил следующие ответы: 
# из n школьников у m домашнее задание съела собака, у k отключили свет, 
# а p учеников постигли оба несчастья. Напишите программу, которая определяет сколько человек выполнило домашнее задание.

n, m, k, p = [int(input()) for _ in range(4)]
print(n + p - m - k)

Sample Input:
35
20
10
3
Sample Output:
8
