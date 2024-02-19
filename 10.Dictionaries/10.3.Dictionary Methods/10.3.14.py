# Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек собак (сохранив исходный порядок следования).
# Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
# Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
# Примечание 3. Выводить содержимое словаря result не нужно.

# You have access to a pets list containing information about dogs and their owners. Each element of the list is a tuple of the type (dog name, owner's name, owner's last name, owner's age).
# Complete the code below so that the result variable stores a dictionary in which for each owner his dogs will be listed. The key of the dictionary should be a tuple (first name, last name, age of the owner), and the value should be a list of dog names (preserving the original order).
# Note 1: Don't forget: tuples are immutable, so they can be dictionary keys.
# Note 2: Please note that some owners have multiple dogs.
# Note 3: There is no need to display the contents of the result dictionary.

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in pets:
    result[i[1:]] = result.get(i[1:], []) + [i[0]]
