import sys
from lesson04 import my_mod

# print(sys.argv) # команда выводит список данных, который содержится в модуле

try:
    file, user, salary = sys.argv
except ValueError:
    print("Invalid args")
    exit()

my_mod.hello(user)
print(my_mod.calculate(int(salary)))