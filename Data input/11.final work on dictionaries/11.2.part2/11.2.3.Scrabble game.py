# Scrabble game
# В игре Scrabble каждая буква приносит определенное количество баллов. 
# Общая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:
# Напишите программу подсчета итоговой стоимости введенного слова.

# In the game Scrabble, each letter is worth a certain number of points. The total value of a word is the sum of the points of its letters. 
# The less often a letter is found, the more valued it is:
# Write a program to calculate the total cost of an entered word.

Баллы	Буква
1	A, E, I, L, N, O, R, S, T, U
2	D, G
3	B, C, M, P
4	F, H, V, W, Y
5	K
8	J, X
10      Q, Z



Scrabble = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
score = 0
for i in input():
    score += Scrabble[i]
print(score)



Sample Input 1:
DANSER
Sample Output 1:
7
Sample Input 2:
FRESHENER
Sample Output 2:
15
Sample Input 3:
ZIP
Sample Output 3:
14
