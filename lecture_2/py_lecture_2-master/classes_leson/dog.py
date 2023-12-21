class Dog:
    """A simple attempt to model a dog."""
    species = "Animal"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self, where):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over " + where)
