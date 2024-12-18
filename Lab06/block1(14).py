import math
def heron_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return None
try:
    a = float(input("длина стороны a: "))
    b = float(input("длина стороны b: "))
    c = float(input("длина стороны c: "))
    area = heron_area(a, b, c)
    if area is not None:
        print(f"треугольник существует. Площадь треугольника: {area:.2f}")
    else:
        print("треугольник с такими сторонами не существует.")
except ValueError:
    print("вводите только числовые значения.")
