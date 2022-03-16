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


john = Person()
artur = User()

john.show_name()
artur.show_name()