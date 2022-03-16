# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivideException(Exception):
    def __init__(self, divisor):
        self.divisor = divisor

    def __str__(self):
        return f"Zero divide error: {self.divisor} = 0"


class Divide:
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivideException(b)
        else:
            return a / b


a = float(input("Please enter divided: "))
b = float(input("Please enter divisor: "))

try:
    print(Divide.divide(a, b))
except ZeroDivideException:
    while b == 0:
        b = float(input("Divisor is 0, Please enter other divisor: "))
    print(Divide.divide(a, b))