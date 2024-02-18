# Number of words in the text
# Write a program to determine the total number of different words in a line of text.
# Note 1. A word is a sequence of non-blank characters in a row, words separated by one or more spaces.
# Note 2. Punctuation marks .,;:-?! neglected.

# Количество слов в тексте
# Напишите программу для определения общего количества различных слов в строке текста.
# Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.

text = input()  #Количество слов в тексте
w = []
for word in text.split():
    w.append(word.lower().strip('.,;:-?!'))
print(len(set(w)))

# Sample Input 1:
# Milk is white and so is glue, Ghosts are white and they say BOO!
# Sample Output 1:
# 11
# Sample Input 2:
# Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.
# Sample Output 2:
# 15
# Sample Input 3:
# Lets make the color pink. Lets make the color pink. Mixing red and white, I think, Well make the color pink.
# Sample Output 3:
# 12
