with open('data.txt', 'w') as printable_file:
    strings = ["John", "Kate"]
    for x in strings:
        print(x, file=printable_file)