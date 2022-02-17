# password = input("введите пароль >>>")
#
# original_password = "correct"
#
# if password == original_password:
#     print("верно")
# else:
#     print("неверно")
#

age = int(input("введите ваш возраст >>>"))

if age >= 14:
    print("паспорт можно получить")

    if 20 <= age < 45:
        print("паспорт можно поменять")
elif age < 1:
    print("custom")
else:
    print("паспорт нельзя получить")