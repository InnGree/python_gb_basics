# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

resume = None
special_cymbol = "stop"
total = 0

def line_calculator(number_list, previous_total=0):
    result = 0
    for line in number_list:
        try:
            number = float(line)
        except ValueError:
            number = 0
        result += number
    return result + previous_total

while resume != special_cymbol:
    user_number_line = input("Please enter numbers delimited by space: ")
    user_number_list = user_number_line.split(" ", maxsplit=-1)
    if user_number_list.count(special_cymbol) == 0:
        sum = line_calculator(user_number_list, total)
        print(sum)
        total = sum
        resume = input(f"Would you like calculate? Enter \"{special_cymbol}\" to exit: ")
    else:
        position = user_number_list.index(special_cymbol)
        new_user_number_list = user_number_list[0:position]
        sum = line_calculator(new_user_number_list, total)
        print(sum)
        break