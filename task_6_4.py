"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        # self.is_police = is_police

    def go(self):
        print('car goes')

    def stop(self):
        print('car stopped')

    def turn(self, direction):
        print('car turned to the left') if direction == 'left' else print('car turned to the right')

    def showspeed(self):
        print(f'current speed is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, capacity, color, name):
        super().__init__(speed, color, name)
        self.is_police = False
        self.capacity = capacity

    def showspeed(self):
        print('over speed limit') if self.speed > 60 else print(f'current speed is {self.speed}')


class SportCar(Car):
    def __init__(self, speed, max_speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False
        self.max_speed = max_speed

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def showspeed(self):
        print('over speed limit') if self.speed > 40 else print(f'current speed is {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
    def catch_car(self, SportCar):
        print('we did it') if self.speed > SportCar.max_speed else print('we need to increase budget')


my_car = Car(60, 'blue', 'my_car')
my_car.turn('right')
my_car.showspeed()

new_car = WorkCar(50, 'yellow', 'Volvo')
new_car.showspeed()

new_sportcar = SportCar(speed=120, max_speed=200, color='red', name='Ferrari')
new_policecar = PoliceCar(speed=100, color='blue', name='Ford')
new_policecar.catch_car(new_sportcar)