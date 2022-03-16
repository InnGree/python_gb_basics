# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, nucleus: int):
        self.nucleus = nucleus

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.nucleus + other.nucleus
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Cell) and self.nucleus > other.nucleus:
            return self.nucleus - other.nucleus
        elif isinstance(other, Cell):
            return f"Substraction is impossible"
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Cell):
            return self.nucleus * other.nucleus
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return self.nucleus // other.nucleus
        else:
            return None

    def make_order(self, count_in_row: int):
        counter = 1
        result = ""
        while counter <= self.nucleus:
            result = result + "*"
            if counter % count_in_row == 0:
                result = result + "\n"
            counter += 1
        return result

my_cell = Cell(35)
new_cell = Cell(25)
print(my_cell + new_cell)
print(my_cell.make_order(5))
