my_file = open('data.txt', "w") # если файл в другой директории, то нужно весь путь.
# Экранирование слэшом лечится либо использованием двух слешей, или добавить перед строкой символ r - r'C:\temp....'

if my_file.writable():
    my_file.write("update\n")
    strings = ["John\n", "Kate\n"]
    my_file.writelines(strings) # заносит значения циклом
else:
    print("Can not write")

my_file.close() # не забываем закрывать потоки