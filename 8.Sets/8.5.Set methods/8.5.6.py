# Какая строка кода приведет к возникновению ошибки?
# Which line of code will cause the error to occur?

my_set = {'a', 'b', 'c'}
 
my_set.discard('a')         # 1
my_set.discard('a')         # 2
my_set.remove('b')          # 3
my_set.remove('b')          # 4

# 4
