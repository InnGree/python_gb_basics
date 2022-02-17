# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

def factor(number: int):
    temp_result = 1

    if number <= 0:
        yield temp_result

    for x in range(1, number + 1):
        temp_result *= x
        yield temp_result


N = 4

for el in fact(N):
    print(el)