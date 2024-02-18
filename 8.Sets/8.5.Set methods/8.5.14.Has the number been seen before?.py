# Has the number been seen before?
# The input to the program is a string of text containing numbers. 
# For each number, print the word YES (in a separate line) if this number has previously appeared in the sequence or NO if it has not.
# Note. Leading zeros in numbers should be ignored.

# Встречалось ли число раньше?
# На вход программе подается строка текста, содержащая числа. 
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
# Примечание. Ведущие нули в числах должны игнорироваться.

n = input().split()
a = []
b = []
for i in range(len(n)):
    if int(n[i]) not in a:
        a.append(int(n[i]))
        b.append('NO')
    else:
        b.append('YES')
for f in b:
    print(f)
  

Sample Input 1:
1 1 2 2 5 5 5 5 6 7 8
Sample Output 1:
NO
YES
NO
YES
NO
YES
YES
YES
NO
NO
NO
Sample Input 2:
10 5 48 6 38 1
Sample Output 2:
NO
NO
NO
NO
NO
NO
Sample Input 3:
1 1 1 1 1 1 1 1 1
Sample Output 3:
NO
YES
YES
YES
YES
YES
YES
YES
YES
Sample Input 4:
1 2 3 002 03 4 5 05
Sample Output 4:
NO
NO
NO
YES
YES
NO
NO
YES
