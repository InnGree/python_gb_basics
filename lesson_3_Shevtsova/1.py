# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_func(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Can't divide by zero"

first_arg = int(input("Divident: "))
sec_arg = int(input("Divisor: "))
print(divide_func(first_arg, sec_arg))

