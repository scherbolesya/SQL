# Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 20. 
# При этом порядок оставшихся элементов меняться не должен.
# Примечание. Необходимо изменить словарь my_dict, выводить ничего не надо.

# Complete the code below so that the lists of values for elements in the my_dict dictionary do not contain numbers greater than 20. 
# However, the order of the remaining elements should not change.
# Note. You need to change the my_dict dictionary, you don't need to print anything.

my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {key: [value[i] for i in range(len(value)) if value[i] <= 20] for key, value in my_dict.items()}
