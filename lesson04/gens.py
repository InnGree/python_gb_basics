import random

tel = "8800123450"

# надо зарезервировать все номера после 50 - сгенерить все номера.

# for x in range(1, 10):
#     return x - ниже аналог этого

tel_list = [f"{tel}{x}" for x in range(1, 10) if x != 5] # в рамках одной строки генерится список

print(tel_list)

numbers = [10, 20, 30, 40]

result_dict = {key: key * 2 for key in numbers}

print(result_dict)

random_number = random.choice(tel_list)
print(random_number)

random.shuffle(tel_list)
print(tel_list)