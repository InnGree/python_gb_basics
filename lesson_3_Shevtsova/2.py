# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой

def user_data(first_name, last_name, birth_date, res_city, email, phone):
    return f"Welcome, {first_name} {last_name}. " \
           f"Your birthday: {birth_date}. " \
           f"You are live in: {res_city}. " \
           f"Your contacts: {email} and {phone}"

user_first_name = input("Your first name: ")
user_last_name = input("Your last name: ")
user_birth_date = input("Your birthday: ")
user_res_city = input("City you live in: ")
user_email = input("Your email: ")
user_phone = input("Your phone: ")

print(user_data(
    first_name=user_first_name,
    last_name=user_last_name,
    birth_date=user_birth_date,
    res_city=user_res_city,
    email=user_email,
    phone=user_phone
    )
)
