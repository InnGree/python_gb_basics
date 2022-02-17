# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 200к, вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('third_exersice.txt') as employees_file:
    lines = [el.split() for el in employees_file.readlines()]
    employee_dict = [{"Last_name": line[0], "Salary": line[1]} for line in lines]
    limit_value = 200000
    total_salaries = 0
    print(f"Employees with salary less then {limit_value} is:")
    for entry in employee_dict:
        total_salaries += float(entry.get("Salary"))
        if float(entry.get("Salary")) < limit_value:
            print(entry.get("Last_name"))
    print(f"Average salary is {total_salaries / len(employee_dict)}")