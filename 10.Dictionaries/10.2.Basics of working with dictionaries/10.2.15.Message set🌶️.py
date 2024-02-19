# Message set 🌶️
# On mobile feature phones, text messages can be sent using the numeric keypad. 
# Because each key has multiple letters associated with it, most letters require multiple keystrokes. 
# Pressing a number once generates the first character specified for that key. Pressing the number 2,3,4 or 5 times generates the second, third, fourth or fifth character of the key.

# Набор сообщений 🌶️
# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. 
# Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. 
# При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2,3,4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.

1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
0	space (пробел)

# Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.
# Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.
# Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в приведенной выше таблице.
# Примечание 3. Nokia 3310, чтобы вспомнить как это было 😄

# Write a program that displays the keystrokes required for an entered message.
# Note 1: Your program must handle both uppercase and lowercase letters.
# Note 2: Your program should ignore any characters not listed in the table above.
# Note 3. Nokia 3310 to remember how it was 😄

d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for letter in input().upper():
    for key, value in d.items():
        if letter in value:
            print(key * (value.index(letter) + 1), end='')


Sample Input 1:
Hello, World!
Sample Output 1:
4433555555666110966677755531111
Sample Input 2:
He said: "I can solve this problem".
Sample Output 2:
44330777724443111110444022226607777666555888330844444777707777666225553361
Sample Input 3:
Bee   Geek!!!
Sample Output 3:
2233330004333355111111111111
