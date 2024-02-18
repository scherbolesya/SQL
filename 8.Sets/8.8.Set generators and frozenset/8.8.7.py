# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка 
# files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений. 
# Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.
# Примечание. Если бы список files содержал следующие имена файлов:
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# то ответом был бы:
# apple.png python.png zebra.png

# Using the set generator, complete the code above so that it selects unique file 
# names with a .png extension from the files list, regardless of case and extensions. 
# Display file names along with extension, all on one line, in lower case, in alphabetical order separated by spaces.
# Note. If the files list contained the following file names:
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# then the answer would be:
# apple.png python.png zebra.png

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
f = set(i.lower() for i in files)
s = set(i for i in f if '.png' in i)
print(*sorted(s))
