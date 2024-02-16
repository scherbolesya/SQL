# Self-written calculator 🌶️
# Write a program that reads two integers and a string from the keyboard. 
# If this line is the designation of one of the four mathematical operations 
# (+, -, *, /), then print the result of applying this operation to the previously entered numbers,
# otherwise print “Invalid operation” (without quotes). If the user wants to divide by zero, display the text 
#“You can’t divide by zero!” (without quotes).

# Самописный калькулятор 🌶️
# Напишите программу, которая считывает с клавиатуры два целых числа и строку. 
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), 
# то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите 
# «Неверная операция» (без кавычек). Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек).

a = int(input())    #заданы 2 числа и знак
b = int(input())
c = input()
if  b == 0 and c == '/':
    print('На ноль делить нельзя!')
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c =='/' and b != 0:
    print(a/b)
else:
    print('Неверная операция')

# Sample Input 1:
# 6104
# 0
# /
# Sample Output 1:
# На ноль делить нельзя!
# Sample Input 2:
# 25
# 5
# *
# Sample Output 2:
# 125
# Sample Input 3:
# 89
# 80
# -
# Sample Output 3:
# 9
# Sample Input 4:
# 567
# 433
# +
# Sample Output 4:
# 1000
