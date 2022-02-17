# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества символов в каждой строке.

with open('second_exercise.txt') as file_for_read:
    lines = file_for_read.readlines()
    print(f"Count of lines: {len(lines)}")
    for ind, line in enumerate(lines):
        ind += 1
        count_of_symbols = len(line)
        if line.endswith("\n"):
            print(f"Number of symbols in line {ind}: {count_of_symbols-1}")
        else:
            print(f"Number of symbols in line {ind}: {count_of_symbols}")
