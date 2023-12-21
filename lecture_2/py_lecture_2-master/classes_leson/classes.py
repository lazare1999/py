from classes_leson.dog import Dog
from classes_leson.jackRusselTerrier import JackRusselTerrier

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over("here")

print(my_dog.name)
print(my_dog.age)
print(my_dog)
print(my_dog.__str__())


my_russel_terrier = JackRusselTerrier('grey', 'willie', 6)
print(my_russel_terrier.run(20))

print(my_russel_terrier)
print(my_russel_terrier.to_str())

