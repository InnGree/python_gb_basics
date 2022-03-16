class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name:str, last_name:str):
        self._first_name = first_name
        self._last_name = last_name

    def full_name(self):
        return f"Person: {self._first_name} {self._last_name}"


john = Person("John", "Doe")
# print(john._first_name)
# _first_name - защищенная переменная, к ней не принято обращаться.
# инкапсуляция заключается в том, что мы не должны знать о том, какие есть переменные класса.Это закрытая логика.
# нам должен быть предложен отдельный видимый метод, который покажет, например, full_name.

print(john.full_name())
