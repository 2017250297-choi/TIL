class Car:
    color = "red"

    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed
        self.speed_limit = speed * 2

    def accelerate(self, dv):
        dv = 0 if 0 > dv else dv
        self.speed = min(self.speed_limit, self.speed + dv)

    def brake(self, dv):
        dv = 0 if 0 > dv else dv
        self.speed = max(0, self.speed - dv)

    def get_speed(self, unit="kph"):
        if unit == "kph":
            return self.speed
        elif unit == "mps":
            return self.speed / 3.6
        else:
            raise ValueError()

    def drive(self):
        print("Brrrr")


my_car = Car("bugati", "blue", 30)
my_car.drive()
import json

a = json.dumps(my_car)
print(str(a))


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}, the animal makes some noise.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        self.dog_breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name}, the dog barks. Bow-Wow!")


class Cat(Animal):
    def __init__(self, name, age, breed):
        self.cat_breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name}, the cat says, Meow Meow!")


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
