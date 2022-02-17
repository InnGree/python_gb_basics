# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

with open('sixth_file.txt') as specialities_file:
    specialities_dict = {}
    for line in specialities_file.readlines():
        numbers = re.findall('[0-9]+', line)
        total = 0
        for number in numbers:
            int(number)
            total += int(number)
        specialty = line.split(":")[0]
        specialities_dict[specialty] = total
    print(specialities_dict)