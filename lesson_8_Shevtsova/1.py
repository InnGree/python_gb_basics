# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re

class Date:
    def __init__(self, date_string: str):
        self.date_str = date_string

    @staticmethod
    def num_export(input_str):
        if re.match(r'\d\d-\d\d-\d\d\d\d', input_str):
            temp = input_str.split("-")
            date_as_nums = []
            for x in temp:
                date_as_nums.append(int(x))
        return date_as_nums

    @classmethod
    def date_validation(cls, input_date):
        values = cls.num_export(input_date)
        day, month, year = values[0], values[1], values[2]
        if 1 > month > 12:
            return False
        elif 1900 > year > 2999:
            return False
        elif (month in (4, 6, 9, 11) and day > 30) or (month == 2 and day > 29) or day > 31:
            return False
        else:
            return True


a = "21-12-1990"
b = "31-02-1992"
print(Date.date_validation(a), Date.date_validation(b))