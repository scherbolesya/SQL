# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
# Примечание. Выводить содержимое словаря result не нужно.

# Complete the above code so that the result variable stores a dictionary in which, for each character in the text string, the number of its occurrences will be counted.
# Note. There is no need to display the contents of the result dictionary.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for num in text:
    result[num] = result.get(num, 0) + 1
