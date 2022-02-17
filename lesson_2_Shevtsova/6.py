# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

key_name = "название"
key_price = "цена"
key_count = "количество"
key_unit = "ед"
issues = []
counter = 1

while True:
    dict = {key_name: input("Введите товар: "),
            key_price: input("Введите цену: "),
            key_count: input("Введите количество: "),
            key_unit: input("Введите единицу измерения: ")
            }

    issues.append(counter)
    issues.append(dict)
    counter += 1
    enter_more = input("Если хотите ввести еще товар, наберите 1: ")

    if enter_more != "1":
        break

print(issues)
print(len(issues))

list_key_names = []
list_key_price = []
list_key_count = []
list_key_unit = []
counter = 1

while counter <= len(issues):
    for key, value in issues[counter].items():
        if key == key_name:
            list_key_names.append(value)
        if key == key_price:
            list_key_price.append(value)
        if key == key_count:
            list_key_count.append(value)
        if key == key_unit:
            list_key_unit.append(value)
    counter += 2

dict_key_names = {key_name: list_key_names}
dict_key_price = {key_price: list_key_price}
dict_key_count = {key_count: list_key_count}
dict_key_unit = {key_unit: list_key_unit}

list_key_count = list(set(list_key_count))
list_key_unit = list(set(list_key_unit))

print(dict_key_names)
print(dict_key_price)
print(dict_key_count)
print(dict_key_unit)
