# named_lambda = lambda name: f"Hello, {name}!!!"
#
# print(named_lambda("John"))

# аналогичный результат, как выше, т.е. сразу запускаем:
print((lambda name: f"Hello, {name}!!!")
      ("John")
)

#  возведение в 2 степень
print((lambda x: x ** 2)
      (2)
)

#  передача неограниченного количества аргументов
print((lambda *numbers: numbers)
      (1,2,3)
)