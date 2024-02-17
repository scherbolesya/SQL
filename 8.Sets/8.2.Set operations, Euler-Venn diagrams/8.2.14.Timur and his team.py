# Timur and his team
# During the summer holidays, Timur and the students of the BEEGEEK online school decided to relax. 
# As a result, n school students went on vacation to the sea, m students went to the village, 
# and k students went to the mountains. It turned out that there were x students in both the village and the sea, 
# and y students in the village and in the mountains. No one managed to visit both the mountains and the sea.

Write a program to determine the number of students in a school if no one was able to visit all three places at once, 
# and z students wrote the DVI in mathematics for admission to Moscow State University, and did not go anywhere.

# Note. n - all the students who went to the sea, m - all the students who went to the village, and k - all the students who went to the mountains.

# Тимур и его команда
# На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. 
# В результате n учеников школы поехали отдыхать на море, m учеников съездили в деревню, 
# а k учеников сходили в горы. Оказалось, что и в деревне, и на море были x учеников, 
# а в деревне и в горах — y учеников. Побывать и в горах, и на море не удалось никому. 

# Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу, 
# а z учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.

# Примечание. n – все ученики, которые поехали на море, m – все ученики, которые съездили в деревню, и k – все ученики, которые сходили в горы.

n = int(input()) # учеников школы поехали отдыхать на море
m = int(input()) #учеников съездили в деревню
k = int(input()) #учеников сходили в горы
x = int(input()) #и в деревне, и на море были x учеников
y = int(input())  #деревне и в горах — y учеников
z = int(input()) #z учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.
print((n-x)+x+(m-x-y)+y+(k-y)+z)

# Sample Input:
# 14
# 16
# 5
# 10
# 3
# 2
# Sample Output:
# 24
