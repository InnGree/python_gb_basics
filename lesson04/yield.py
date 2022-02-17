def user_generator():
    for user in {"Artur", "Kate", "John"}:
        yield user
    # цикл не заходит до конца без нашей просьбы

# print(user_generator())
# <generator object user_generator at 0x10419dfc0>

for user_item in user_generator():
    print(user_item)

# след элементы можно получать не только циклом, но и спец.функции next. когда элементы кончатся,
# будет ошибка StopIteration, которую можно обработать

