# Дополните приведенный код так, чтобы переменная new_tuples содержала список кортежей на основе списка tuples с последним элементом каждого кортежа, замененным на численное значение 100.

# Complete the code above so that the new_tuples variable contains a list of tuples based on the tuples list, with the last element of each tuple replaced by a numeric value 100.

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples =  [i[:-1]+(100,) for i in tuples if i]
print(new_tuples)
