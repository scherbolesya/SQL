# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.

# Morse code uses dashes and dots to represent numbers and letters.
# Write a program to encode a text message using Morse code.

Символ   Код  Символ Код  Символ    Код	 Символ	 Код
A        .-    J    .---      S    ...    1    .----
B        -...  K    -.-	      T     -	  2    ..---
C        -.-.  L    .-..      U    ..-    3    ...--
D        -..   M    --        V    ...-   4    ....-
E        .     N    -.        W    .--    5    .....
F        ..-.  O    ---       X    -..-   6    -....
G        --.   P    .--.      Y	   -.--   7    --...
H        ....  Q    --.-      Z    --..   8    ---..
I        ..    R    .-.       0    -----  9    ----.

# Примечание 1. Ваша программа должна игнорировать любые символы, не перечисленные в таблице.
# Примечание 2. Код Морзе был разработан в XIX веке и все еще используется, спустя более 160 лет после создания.

# Note 1: Your program should ignore any symbols not listed in the table.
# Note 2: Morse code was developed in the 19th century and is still in use more than 160 years after its creation.

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))
for s in input().upper():
    for key, value in d.items():
        if s in key:
            print(value, end=" ")
  
Sample Input 1:
Interstellar
Sample Output 1:
.. -. - . .-. ... - . .-.. .-.. .- .-.
Sample Input 2:
SOS
Sample Output 2:
... --- ...
Sample Input 3:
Agent 007
Sample Output 3:
.- --. . -. - ----- ----- --...
