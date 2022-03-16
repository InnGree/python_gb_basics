class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name:str, last_name:str):
        self._first_name = first_name
        self._last_name = last_name

    def full_name(self):
        return f"{self._first_name} {self._last_name}"


class User(Person):
    login: str
    password: str

    def __init__(self, first_name: str, last_name: str, login: str):
        super().__init__(first_name, last_name)  # получаем то, что заложено в родительском классе
        self.login = login  # переопределили метод, добавив переменную.

    def log_in(self):
        print(f"Welcome, {self.full_name()}!")


class InfoPrinter:
    def info(self, class_object):
        if isinstance(class_object, User):
            print("It's a User")
        elif isinstance(class_object, Person):
            print(f"It's a Person")
        else:
            print("Unknown class/type")


john = User("John", "Doe", "john_doe")
john.log_in()

artur = Person("Artur", "Doe")

printer = InfoPrinter()

printer.info(artur)
printer.info(john)
printer.info([])
