class Person:
    _name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._name = first_name
        self._last_name = last_name

    @property # эта штука делает для обращения вне класса из full_name атрибут, а не функцию
    def full_name(self):
        return f"{self._name} {self._last_name}"

john = Person("John", "Doe")

print(john.full_name)