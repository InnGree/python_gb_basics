user = {'name': 'John'}

try:
    print(user["age"])
except KeyError:
    print("Key is invalidovna")

try:
    a = 100/0
except ZeroDivisionError:
    print("Zero, lopux!")