# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if x > 0 and y < 0 and y % 1 == 0:
        # первый вариант:
        # return x ** y
        # второй вариант:
        result = 1
        counter = y
        while counter < 0:
            result = result * x
            counter += 1
        return 1 / result
    else:
        return f"Pair {x} and {y} doesn't meet the conditions"

try:
    x = float(input("Insert x:"))
    y = int(input("Insert y:"))
    print(my_func(x, y))
except ValueError:
    print("You entered non-numerical values")

