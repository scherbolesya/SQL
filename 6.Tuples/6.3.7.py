# Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.

# Complete the following code so that it produces a list containing the arithmetic means of the numbers of each nested tuple in the given tuple of numbers tuples.

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
a = []
for i in numbers:
    a.append(sum(i)/(len(i)))
print(a)
