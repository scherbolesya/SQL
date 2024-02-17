# Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.

# Complete the code above to produce a list containing only the non-empty tuples of the original tuples list, without changing their order.

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i != ()] 
print(non_empty_tuples)
