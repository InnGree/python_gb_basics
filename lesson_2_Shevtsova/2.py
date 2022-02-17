# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

list_len = int(input("Задайте количество элементов: ")) - 1

list_by_user = []

while list_len >= 0:
    element = input("Добавьте значение в список: ")
    list_by_user.append(element)
    list_len -= 1

list_len = len(list_by_user) - 1
counter = 0

while counter < list_len:
    temp_element = list_by_user[counter]
    list_by_user[counter] = list_by_user[counter + 1]
    list_by_user[counter + 1] = temp_element
    counter = counter + 2

print(list_by_user)