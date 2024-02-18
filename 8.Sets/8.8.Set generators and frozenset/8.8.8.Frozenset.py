# Frozenset

myset1 = frozenset({1, 2, 3})                         # на основе множества
myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
myset3 = frozenset('aabcccddee')                      # на основе строки

print(myset1)
print(myset2)
print(myset3)

выводит:

frozenset({1, 2, 3})
frozenset({1, 2, 3, 4, 5, 6})
frozenset({'e', 'd', 'c', 'b', 'a'})

---------------------------------
myset1 = frozenset('hello')
myset2 = frozenset('world')

print(myset1 | myset2)
print(myset1 & myset2)
print(myset1 ^ myset2)

выводит:

frozenset({'l', 'w', 'e', 'h', 'r', 'd', 'o'})
frozenset({'l', 'o'})
frozenset({'d', 'h', 'w', 'e', 'r'})

-------------------------------
Приведенный ниже код:

sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'

words = sentence.lower().replace('.', '').replace(',', '').split()

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}

print(*consonants, sep='\n')
выводит (порядок элементов может отличаться):

frozenset({'d', 'h'})
frozenset({'h', 't'})
frozenset({'n', 'h', 'g', 't'})
frozenset({'n'})
frozenset({'c', 't'})
frozenset({'n', 'd'})
frozenset({'w', 't'})
frozenset({'s', 'c', 'k', 'd'})
