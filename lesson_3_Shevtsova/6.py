# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    return word.capitalize()


print(int_func("text"))

user_line = input("Please enter the line(use lowercase latin characters): ")
line_list = user_line.split(" ", maxsplit=-1)
new_line = ""

for word in line_list:
    new_line = new_line + int_func(word) + " "

print(new_line)

