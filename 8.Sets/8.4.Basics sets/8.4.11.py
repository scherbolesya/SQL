# Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, 
# отсортированные по убыванию (в обратном лексикографическом порядке).
# Примечание. Выводите каждый элемент множества на отдельной строке.

# Complete the code below to print the elements of the fruits set, each on a separate line, sorted in descending order (in reverse lexicographic order).
# Note. Print each element of the set on a separate line.

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sortfruits = sorted(fruits, reverse=True)
print(*sortfruits, sep='\n')
