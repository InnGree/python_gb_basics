# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce
my_list = [x for x in range(100, 1001) if x % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)
print(my_list)
print(result)