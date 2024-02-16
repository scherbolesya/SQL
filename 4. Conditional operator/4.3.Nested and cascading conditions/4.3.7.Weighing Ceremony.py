# Weighing Ceremony
# The weight of an amateur boxer is known (integer).
# It is known that the weight is such that a boxer can be classified into one of three weight categories:

# Light weight – up to 60 kg (inclusive);
# Welterweight - up to 64 kg (inclusive);
# Welterweight – up to 69 kg (inclusive).
# Write a program that determines in which category a given boxer will compete.

# Церемония взвешивания
# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:

# Легкий вес – до 60 кг (невключительно);
# Первый полусредний вес – до 64 кг (невключительно);
# Полусредний вес – до 69 кг (невключительно).
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

v = int(input()) #определяет вес
if v < 60:
    print('Легкий вес')
elif 60 == v or v < 64:
    print('Первый полусредний вес')
elif 64 == v or v < 69:
    print('Полусредний вес')
  
# Sample Input 1:
# 55
# Sample Output 1:
# Легкий вес
# Sample Input 2:
# 68
# Sample Output 2:
# Полусредний вес
# Sample Input 3:
# 60
# Sample Output 3:
# Первый полусредний вес
