class Human:
    age: int
    first_name: str
    last_name: str
    weight: int
    _password: int
    __bank_account: str

    counter: int = 0  # Глобальная переменная

    def __init__(self, first_name, last_name, age, weight=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self._init_password()
        self.__bank_account = "10000005"

        Human.counter += 1

    def info(self):
        print(f"I am {self.first_name}, age: {self.age}, weight: {self.weight}")

    def _init_password(self):
        self.password = "12314546"

    def show_bank_account(self):
        print(f"Account is {self.__bank_account[:5]}*******")

john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)

john.info()
artur.info()
# Human.info(john) - на самом деле примерно так(self).
print(john.counter)
print(artur.counter)
print(Human.counter)

print(john.show_bank_account())