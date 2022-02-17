users = ["John", "Arthur", "Kate", "Jane"]

def say_hello(*users_list):
    for user in users_list:
        print(user)

say_hello(*users)
# * в функции перед аргументом значит, что любой агрумент, который будет передан как позиционный, будет записан в качестве списка

# дополнение:
# def say_hello(*users_list,**user_settings):
#     for user in users_list:
#         print(user)
#
# say_hello(*users, discount=10, discount=10)
# все что будет указано без звездочки, будет записано в user_settings - второй позиционный аргумент