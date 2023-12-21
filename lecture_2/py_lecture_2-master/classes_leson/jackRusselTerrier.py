from classes_leson.dog import Dog


class JackRusselTerrier(Dog):

    def __str__(self):
        return f"{self.name} is {self.age} years old and it's color is {self.__color}"

    def __init__(self, color, name, age):
        super().__init__(name, age)
        self.__color = color

    def run(self, speed):
        return f"{self.name} The dof runs at running speed of {speed} km/h"

    def to_str(self):
        return super().__str__()

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color



