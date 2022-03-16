class Printable:
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Person(Printable):
    def __init__(self, name):
        self.name = name


john = Person("John")
print(john)