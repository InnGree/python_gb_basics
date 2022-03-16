# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f"{self.name} is moving"

    def stop(self):
        return f"{self.name} is stop"

    def turn(self, direction: str):
        return f"{self.name} turned {direction}"

    def show_speed(self):
        return f"{self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Warning! Over speed!"
        else:
            return f"{self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Warning! Over speed!"
        else:
            return f"{self.speed}"


class PoliceCar(Car):
    is_police = True


nyc_police_1 = PoliceCar(50, "white", "Ford Explorer")
soc_dep_2 = WorkCar(70, "blue", "Nissan X-Trail")
private_car_3 = TownCar(55, "black", "Honda CR-V")

print(f"Speed info: {nyc_police_1.show_speed()}")
print(f"Speed info: {soc_dep_2.show_speed()}")
print(f"Speed info: {private_car_3.show_speed()}")

print(nyc_police_1.turn("left"))
print(soc_dep_2.go())