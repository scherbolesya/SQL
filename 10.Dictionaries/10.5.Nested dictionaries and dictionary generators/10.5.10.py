# В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.
# Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).
# Примечание 2. Выводить содержимое словаря result не нужно.

# The variable s stores a string of number:word pairs. Complete the following code using a generator to produce a result dictionary with numbers as keys and words as values.
# Note 1. Dictionary keys must be integers (int type), values must be strings (str type).
# Note 2: There is no need to display the contents of the result dictionary.

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i.split(':')[0]): str(i.split(':')[1]) for i in s.split()}
