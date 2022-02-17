import json

with open('person.json', 'r') as file_stream:
    person = json.load(file_stream)
    print(sum(person['salaries']))

# print(json.loads('{"name": "John", "age": 40, "salaries": [100, 200, 160]}')) # если получили данные как строку,
# можно использовать loads