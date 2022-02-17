import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

current_dir = '.'
files = os.listdir(current_dir)

for x in files:
    # print(os.path.dirname(x)) # абсолютный путь
    # print(os.path.dirname(f"./{x}")) # относительный путь
    print(os.path.isdir(x))
    print(os.path.split(x))
    # print(os.path.isdir(f"./{x}"))

print(os.path.join('etc/hosts', 'file', 'hop', '1.txt'))