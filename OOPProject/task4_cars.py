class Car:
    def __init__(self, car_speed, car_color, car_name, is_police=False):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = is_police
        if self.speed > 0:
            self.go(self.speed)

    def set_police(self):
        self.is_police = True

    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} начал движение со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')

    def change_speed(self, change):
        self.speed += change
        print(f'Автомобиль {self.name} изменил скорость')


class TownCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч', end=' ')
        if self.speed > 60:
            print(f'и превышает скорость на {self.speed - 60} км/ч!')
        else:
            print()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч', end=' ')
        if self.speed > 40:
            print(f'и превышает скорость на {self.speed - 40} км/ч!')
        else:
            print()


class PoliceCar(Car):
    def __init__(self, car_speed, car_color, car_name):
        super().__init__(car_speed, car_color, car_name, is_police=True)


toyota_car = Car(100, 'red', 'Toyota')
mazda_car = TownCar(85, 'white', 'Mazda')
mazda_car.show_speed()
volkswagen_car = WorkCar(30, 'blue', 'Volkswagen')
volkswagen_car.show_speed()
volkswagen_car.change_speed(15)
volkswagen_car.show_speed()
police_car = PoliceCar(110, 'white', 'Ford')
print(police_car.is_police)
print(mazda_car.is_police)



