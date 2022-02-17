# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

file, hours_worked, rate_per_hour, bonus = argv

try:
    salary = int(hours_worked) * int(rate_per_hour) + int(bonus)
    print(salary)
except ValueError:
    print("Non number value")

