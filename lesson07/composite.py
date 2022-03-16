from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod # некая пометка перед вызовом showname
    def show_name(self):
        pass


class Person(AbstractUser):

    def show_name(self):
        print(f"Its a Person")


class User(AbstractUser):

    def show_name(self):
        print(f"Its a User")


class CompositeUser(AbstractUser): # это будет хранилищем классов, у которых можно вызвать эти методы
    def __init__(self, children: list):
        self.children = children

    def show_name(self):
        for item in self.children: # может использоваться например для уведомлений(на тел, на комп, в смс)
            item.show_name()

a = Person()
b = User()

compositer = CompositeUser([a, b])

compositer.show_name()