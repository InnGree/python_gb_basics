# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

try:
    new_element = int(input("Insert new element: "))
except ValueError:
    print("Please insert a digit")

my_list.append(new_element)
new_list = my_list.sort(reverse=True)

print(my_list)

