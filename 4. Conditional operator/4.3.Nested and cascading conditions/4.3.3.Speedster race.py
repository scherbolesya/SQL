# Speedster race
# Zoom challenged Flash and offered him a fair fight in the form of a race around the magnetar. 
# If he loses, this neutron star will charge and destroy the world, so Flash decided not to take risks without a reason and 
#ask his friend Cisco Ramon if there is any point in accepting the challenge. Cisco received data that Zoom's speed is n, and Flash's speed is k.

# Гонка спидстеров
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. 
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать 
# без причины и узнать у своего друга Циско Рамона, есть ли смысл принимать вызов. Циско получил данные, 
# что скорость Зума равна n, а скорость Флэша равна k.

n, k = int(input()), int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
elif n == k:
    print("Don't know")
  
# Sample Input 1:
# 2204
# 1505
# Sample Output 1:
# NO
# Sample Input 2:
# 2344
# 4324
# Sample Output 2:
# YES
# Sample Input 3:
# 2500
# 2500
# Sample Output 3:
# Don't know
