# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Drawing"


class Pen(Stationery):
    def draw(self):
        return f"{self.title} is drawing"


class Pencil(Stationery):
    def draw(self):
        return f"{self.title} is drawing"


class Handle(Stationery):
    def draw(self):
        return f"{self.title} is drawing"


pen1 = Pen("Parker")
pencil1 = Pencil("Faber-Castell")
nandle1 = Handle("Copic")

print(f"{pen1.draw()}\n{pencil1.draw()}\n{nandle1.draw()}\n")