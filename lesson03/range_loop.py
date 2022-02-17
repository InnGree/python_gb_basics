# counter = 0
#
# while counter < 10:
#     print(counter)
#     counter += 1

# то же самое что и выше, но короче:
for x in range(10, 20, 2):
    print(x)

# преобразование range в список
print(list(range(5)))