# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(first_arg, second_arg, third_arg):
    values = [first_arg, second_arg, third_arg]
    try:
        values.sort(reverse=True)
        return values[0] + values[1]
    except TypeError:
        return "This is not a numbers"

print(my_func(-3,1,12))