with open('data.txt') as my_file:
    print(my_file.read())

print(type((my_file)))

# Exception handler
try:
    with open('data.txt') as my_file:
        print(my_file.read())
except IOError:
    print("Some error")

