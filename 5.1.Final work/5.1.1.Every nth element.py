# Every nth element (step)
# The input to the program is a text string containing characters and the number n. 
# A list is formed from this string. Write a program that splits a list into nested 
# sublists such that n consecutive elements belong to different sublists.

# Каждый n-ый элемент (шаг)
# На вход программе подается строка текста, содержащая символы и число n. 
# Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так, 
# что n последовательных элементов принадлежат разным подспискам.

def chun(s, n): 
    list = []
    for i in range(n):
        list.append(s[i::n])
    return list
s = input().split()   
n = int(input())
print(chun(s, n))

# Sample Input 1:
# a b c d e f g h i j k l m n
# 3
# Sample Output 1:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] 
# Sample Input 2:
# a b c d e f g h i j k l m n
# 2
# Sample Output 2:
# [['a', 'c', 'e', 'g', 'i', 'k', 'm'], ['b', 'd', 'f', 'h', 'j', 'l', 'n']]
# Sample Input 3:
# a b c d e f g h i j k l m n
# 1
# Sample Output 3:
# [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']]
