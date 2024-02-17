# Дополните приведенный код так, чтобы он вывел произведение элементов кортежа numbers.
# Complete the code below so that it prints the product of the elements of the numbers tuple.

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
b = 1
for i in range(len(numbers)):
    b *=numbers[i]
print(b)
