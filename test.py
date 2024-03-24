class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}, the {self.__name__} makes some sound.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        self.dog_breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name}, the {self.__class__.__name__} barks. Bow-Wow!")


class Cat(Animal):
    def __init__(self, name, age, breed):
        self.cat_breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name}, the {self.__class__.__name__} says, Meow Meow!")


kate = Dog('kate', 10, 'Huski')
danny = Cat('danny', 5, 'short-hair')
kate.speak()
danny.speak()
