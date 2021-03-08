"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f"{self.color} {self.name} начал движение")
        else:
            print(f"{self.color} {self.name} не начал движение")

    def stop(self):
        if self.speed == 0:
            print(f"{self.color} {self.name} остановился")
        else:
            print(f"{self.color} {self.name} не остановился")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")


class TownCar(Car):
    speed_limit = 60

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость: {self.speed} км/ч, \nпревышение на {self.speed - self.speed_limit} км/ч')
        else:
            print(f"Скорость: {self.speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость: {self.speed} км/ч, \nпревышение на {self.speed - self.speed_limit} км/ч')
        else:
            print(f"Скорость: {self.speed} км/ч")


class PoliceCar(Car):
    pass


# MyCar = Car(65, "красный", "ВАЗ 2101")
# MyCar.turn("направо")
# MyCar.go()
# MyCar.stop()
# MyCar.show_speed()

MyTownCar = TownCar(65, "зелёный", "ВАЗ 2101")
MyTownCar.show_speed()
MyWorkCar = WorkCar(41, "оранжевый", "ВАЗ 2102")
MyWorkCar.show_speed()
print(f"Скорость рабочего автомобиля: {MyWorkCar.speed}")
