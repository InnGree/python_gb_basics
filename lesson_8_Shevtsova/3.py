# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NonNumException(Exception):
    def __init__(self, entered_value):
        self.entered_value = entered_value

    def __str__(self):
        return f"{self.entered_value} is not a digit"


list_of_numbers = []
value = ""
while True:
    value = input("Please enter a number: ")

    if value == "stop":
        break

    try:
        if not(value.isdigit()):
            raise NonNumException(value)
        list_of_numbers.append(int(value))
    except NonNumException as exception:
        print(exception)
print(list_of_numbers)

