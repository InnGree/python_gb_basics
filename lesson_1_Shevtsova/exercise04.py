# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите число:"))
new_digit = number % 10 # 6
max_digit = new_digit

while max_digit < number:
    number = (number - new_digit) / 10

    if number % 10 == 0:
            number = number / 10

    if number < 10:
        if number > max_digit:
            max_digit = number

    new_digit = number % 10

    if max_digit < new_digit:
        max_digit = new_digit

print(max_digit)





