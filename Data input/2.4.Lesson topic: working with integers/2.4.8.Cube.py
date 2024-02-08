# Напишите программу, вычисляющую объем куба и площадь его полной поверхности по введенному значению длины ребра.
# Write a program that calculates the volume of a cube and its total surface area using the entered edge length.

# Sample Input 3:
# 56
# Sample Output 3:
# Объем = 175616
# Площадь полной поверхности = 18816 

# Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3, \, \, S = 6a^2
d = int(input()) #длинна ребра
v = d**3
s = 6*d**2
print('Объем =', v )
print('Площадь полной поверхности =', s) 
