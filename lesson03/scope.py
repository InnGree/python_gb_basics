# 1 пример - ЛОКАЛЬНАЯ:
# numer = 1
#
# def increment():
#     number += 1
#
# increment()
# Ошибка при запуске: UnboundLocalError: local variable 'number' referenced before assignment
# Причина - number в функции виден только внутри функции.

# функция не меняет значение number, даже если оно передается внутрь.
# number = 1
#
# def increment(a):
#     print(a)
#     a += 1
#     print(a)
#
# increment(number)
# print(number)

# 2 пример ГЛОБАЛЬНАЯ: для result прописано что она глобальна, и ее можно использовать вне функции.
# number = 1
#
# def increment(a):
#     global result
#     result = a + 1
#     print(result)
#
#
# increment(number)
# print(number)
# print(result)

# Но! Опасность в том, что если вдруг что-то пойдет не так внутри функции, и в ней будет операция не о том, что нужно,
# то будет получена ошибка. Поэтому код закоментился и используется слово pass как заглушка,
# чтобы другой разработчик понимал, что тут надо написать код:

# number = 1
#
# def increment(a):
#     # global result
#     # result = a + 1
#     # print(result)
#     pass
#
# increment(number)
# print(result)

# 3 пример - НЕ ЛОКАЛЬНАЯ

def top_func():
    start = 0

    def inner_func():
        nonlocal start
        start += 1

    inner_func()
    print(start)

top_func()
