# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

phrase = input("What would you like to say? ")

phrase_list = phrase.split(" ")

count_of_words = len(phrase_list)
number = 0

while count_of_words > 0:
    word = phrase_list[number]
    print(number + 1, word[:10])
    number += 1
    count_of_words -= 1
