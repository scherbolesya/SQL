# Three words
# The input to the program is a string consisting of three words. Is it true that the same set of letters was used to write all three words?

# Три слова
# На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

n,m,k = input().split()
print('YES' if set(n) == set(m) == set(k) else 'NO')

# Sample Input 1:
# автор товар отвар
# Sample Output 1:
# YES
# Sample Input 2:
# шарада баллада услада
# Sample Output 2:
# NO
# Sample Input 3:
# сорт торс трос
# Sample Output 3:
# YES
# Sample Input 4:
# клоун кулон уклон
# Sample Output 4:
# YES
