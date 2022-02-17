# Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [
    el for i, el in enumerate(my_list) if i > 0 and my_list[i - 1] < el
]

print(my_list)
print(new_list)