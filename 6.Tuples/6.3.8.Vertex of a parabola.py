# Vertex of a parabola
# The parabola equation is y = a x 2 + b x + c y =ax 2 +bx+c, gde a ≠ 0. Write a program that, based on the entered values of a, b, c, determines and displays the vertex of a parabola.

# Вершина параболы
# Уравнение параболы имеет вид y = a x 2 + b x + c y =ax 2 +bx+c, gde a ≠ 0. Напишите программу, которая по введенным значениям a,b,c определяет и выводит вершину параболы.

a,b,c = int(input()),int(input()),int(input())
x = -b/(2*a)
y = ((4*a*c-b*b)/(4*a))
print((x,+ y))

# Sample Input 1:
# -2
# 6
# 1
# Sample Output 1:
# (1.5, 5.5)
# Sample Input 2:
# -5
# 2
# 0
# Sample Output 2:
# (0.2, 0.2)
# Sample Input 3:
# 2
# 4
# -5
# Sample Output 3:
# (-1.0, -7.0)
