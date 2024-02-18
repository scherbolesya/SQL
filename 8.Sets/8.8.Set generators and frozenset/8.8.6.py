# Используя генератор множеств, дополните приведенный код так, чтобы получить множество, 
# содержащее уникальные слова  строки sentence длиною меньше 4 символов. 
# Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.
# Примечание. Учтите, что знаки пунктуации не относятся к словам.

# Using a set generator, complete the following code to create a set 
# containing the unique words of sentence that are less than 4 characters long. 
# Print the result on one line (in lowercase) in alphabetical order, separating elements with one space character.
# Note. Please note that punctuation marks do not apply to words.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
a = {i.strip(':,.!?();').lower() for i in sentence.split()}
b = {i for i in a if len(i) < 4}
print(*sorted(b))
