# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите количество секунд:"))
minutes = 0
hours = 0

if 60 <= seconds < 3600:
    minutes = seconds // 60
    seconds = seconds % 60

if seconds >= 3600:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60

if minutes < 10:
        minutes = f"0{minutes}"

if hours < 10:
        hours = f"0{hours}"

if seconds < 10:
    seconds = f"0{seconds}"

print(f"{hours}:{minutes}:{seconds}")