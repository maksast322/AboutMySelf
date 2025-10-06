from math import pi 



dlina = int(input("Введите длину прямоу-ка: "))
shirina = int(input("Введите ширину прямоу-ка: "))

result = dlina * shirina

rad = int(input("Введите радиус: "))

result = pi * rad ** 2
print(round(result, 2))