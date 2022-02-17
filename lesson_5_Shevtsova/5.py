# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('fifth_file.txt', 'w') as digit_set:
    digit_set.write("1 2 3 4 5")

with open('fifth_file.txt') as numbers:
    numbers_list = numbers.readline().split(" ")
    total = 0
    for x in numbers_list:
        total += int(x)
    print(total)

