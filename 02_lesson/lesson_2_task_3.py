import math

print(math.ceil(1.1))


def square(x):
    square = x**2
    return (square)


x = float(input("Сторона квадрата:"))
result = square(x)
rounded = math.ceil(result)
print(rounded)
