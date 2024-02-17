# Queen moves
# There is a queen on an 8x8 chessboard. Mark the position of the queen on the board and all the squares that the queen captures. 
# The square where the queen stands is marked with the letter Q, the squares that the queen is beating are marked with *, and the remaining squares are filled with dots.

# Ходы ферзя
# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. 
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.

col = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
row = ('8', '7', '6', '5', '4', '3', '2', '1')
doska = [['.']*8 for i in range(8)]

def hodkonya(s):     
    y = col.index(s[0])
    x = row.index(s[1])
    
    for i in range(8):
        for j in range(8):
            if abs(i-x)==abs(j-y) or x==i or y==j:
                doska[i][j] = '*'
    doska[x][y] = 'Q'            
    for d in doska:
        print(*d)
        
s = input()
hodkonya(s)

# Sample Input 1:
# c4
# Sample Output 1:
# . . * . . . * .
# . . * . . * . .
# * . * . * . . .
# . * * * . . . .
# * * Q * * * * *
# . * * * . . . .
# * . * . * . . .
# . . * . . * . .

# Sample Input 2:
# a1
# Sample Output 2:
# * . . . . . . *
# * . . . . . * .
# * . . . . * . .
# * . . . * . . .
# * . . * . . . .
# * . * . . . . .
# * * . . . . . .
# Q * * * * * * *

# Sample Input 3:
# h5
# Sample Output 3:
# . . . . * . . *
# . . . . . * . *
# . . . . . . * *
# * * * * * * * Q
# . . . . . . * *
# . . . . . * . *
# . . . . * . . *
# . . . * . . . *
