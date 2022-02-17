# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

chosen_month = int(input("Insert month number: "))

# 1. Решение через list
# winter_list = [1, 2, 12]
# spring_list = [3, 4, 5]
# summer_list = [6, 7, 8]
# autumn_list = [9, 10, 11]
#
# for number in winter_list:
#     if number == chosen_month:
#         print("It's winter")
#
# for number in spring_list:
#     if number == chosen_month:
#         print("It's spring")
#
# for number in summer_list:
#     if number == chosen_month:
#         print("It's summer")
#
# for number in autumn_list:
#     if number == chosen_month:
#         print("It's autumn")

# 2. Решение через dict
season_dict = {
    "Winter": [1, 2, 12]
    , "Spring": [3, 4, 5]
    , "Summer": [6, 7, 8]
    , "Autumn": [9, 10, 11]
}

for key, value in season_dict.items():
    for month in value:
        if month == chosen_month:
            print(key)

