# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list: list):
        self.list = list

    def __str__(self):
        matrix_length = len(self.list[0])
        counter = 0
        line = ""

        while counter < matrix_length:
            for l in self.list:
                line = line + str(l[counter]) + " "
            line = line + "\n"
            counter += 1
        return line

    def __add__(self, other):
        counter = 0
        while counter < len(self.list):
            temp_list = [x + y for x, y in zip(self.list[counter], other.list[counter])]
            self.list[counter] = temp_list
            counter += 1
        return self


my_matrix = Matrix([[2, 3, 4],
                    [5, 7, 8],
                    [9, 6, 1]
                    ])

other_matrix = Matrix([[1, 1, 1],
                       [2, 2, 2],
                       [3, 3, 3]
                       ])

print(my_matrix)
print(other_matrix)
print(my_matrix + other_matrix)


