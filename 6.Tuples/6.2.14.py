# В переменную city_name вводится название города (например, Москва), а в переменную city_year – год его основания (например, 1147). 
# Заполните пропущенную строку таким образом, чтобы в переменной city оказался кортеж из значений этих двух переменных (сначала название города, затем год основания).

# The name of the city is entered into the city_name variable (for example, Moscow), and the year of its foundation is entered into the city_year variable (for example, 1147). 
# Fill in the missing line so that the city variable contains a tuple of the values of these two variables (first the name of the city, then the year of foundation).

city_name = input()
city_year = int(input())
city = (city_name, + city_year)
print(city)
