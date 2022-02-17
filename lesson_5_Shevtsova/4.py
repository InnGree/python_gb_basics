# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('fourth_file.txt') as counter_file:
    dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    new_list = []
    for line in counter_file.readlines():
        word, line = line.split(" — ")
        for key, value in dict.items():
            if word == key:
                new_list.append(value + " — " + line)
    with open('fourth_new_file.txt', 'w') as new_file:
        new_file.writelines(new_list)
