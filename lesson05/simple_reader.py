my_file = open('data.txt') # если файл в другой директории, то нужно весь путь.
# Экранирование слэшом лечится либо использованием двух слешей, или добавить перед строкой символ r - r'C:\temp....'

# for line in my_file.readlines():
#     print(line.replace("\n", ""))
#     # заменяем перенос строки, чтоб не дублирвоался
#
# print(my_file.read())
# при read возвращается одна строка.

print(my_file.closed)
print(my_file.mode)
print(my_file.name)

# чтобы уберечься от переполнения памяти, лучше указать байты и обрабатывать порциями-
for data in my_file.read(1024):
    print(data)

# print(my_file.tell())
#
# my_file.seek(0, 0)
#
# print(my_file.tell())

my_file.close() # не забываем закрывать потоки