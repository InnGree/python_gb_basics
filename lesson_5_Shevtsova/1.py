# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    with open('first_exercise.txt', 'w') as file_to_write:
        user_line = input("Please insert text: ")
        if not user_line:
            break
        file_to_write.write(f"{user_line}\n")
