# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open('seventh_file.txt') as firms_data:
    total_revenue = 0
    firm_revenue_dict = {}
    avg_rev_dict = {}
    for line in firms_data:
        line = line.replace("\n", "")
        new_list = line.split(" ")
        revenue = int(new_list[2]) - int(new_list[3])
        firm_revenue_dict[new_list[0]] = revenue
        print(f"Revenue of {new_list[0]}:{revenue}")
        if revenue > 0:
            total_revenue += revenue
    avg_rev_dict["Average profit"] = total_revenue/len(new_list)
    print(f"Average revenue: {total_revenue/len(new_list)}")
    total_list = [firm_revenue_dict, avg_rev_dict]
    print(total_list)

    with open('firms_and_revenue.json', 'w') as file_stream:
        json.dump(total_list, file_stream)