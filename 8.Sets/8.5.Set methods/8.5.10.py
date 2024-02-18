# Что будет выведено в результате выполнения следующего программного кода?
# What will be the output of the following code?

myset = set()
for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')
print(len(myset))

# 2
