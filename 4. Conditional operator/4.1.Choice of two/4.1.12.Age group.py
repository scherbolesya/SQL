# Age group
# Возрастная группа

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 (включительно) – детство;
# от 14 до 24 (включительно) – молодость;
# от 25 до 59 (включительно) – зрелость;
# от 60 – старость.

# up to 13 (inclusive) – childhood;
# from 14 to 24 (inclusive) – youth;
# from 25 to 59 (inclusive) – maturity;
# from 60 – old age.

a = int(input()) 
if a <= 13:
    print('детство')
if a >= 14 and a <= 24:
    print('молодость')
if 25 <= a <= 59:
    print('зрелость')
if a>60:
    print('старость')

# Sample Input 1:
# 4
# Sample Output 1:
# детство
# Sample Input 2:
# 91
# Sample Output 2:
# старость
# Sample Input 3:
# 40
# Sample Output 3:
# зрелость
