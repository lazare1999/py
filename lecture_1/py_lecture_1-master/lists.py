bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 3-1. Names:
names = ['lazo', 'luka', 'mari']
for n in names:
    print(n)

# 3-2. Greetings:
for n in names:
    print("I love " + n)

# 3-3. Your Own List:
transports = ['Honda motorcycle', 'vw sedan']
for t in transports:
    print("I would like to own a " + t)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# 3-4. Guest List:

guests = ['lazo', 'luka', 'mari']
for g in guests:
    print(g + ", can u come tonight?")

# 3-5. Changing Guest List:
for g in guests:
    if g == 'luka':
        print(g + ", is busy")

guests[1] = 'gigi'
for g in guests:
    print(g + " is coming")

# 3-6. More Guests:
for g in guests:
    print(g + " i have bigger dinner table than i imagined")

guests.insert(0, 'elene')
guests.insert(2, 'salome')
guests.append('kowo')

for g in guests:
    print(g + " is coming")

# 3-7. Shrinking Guest List:
for g in guests:
    print(g + " i only have 2 place , apparently")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(removed_guest + " no longer invited")

for g in guests:
    print(g + " u are coming")

del guests[0]
del guests[0]

print(guests)

# Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 3-8. Seeing the World:
places = ['japan', 'america', 'gb', 'germany', 'italy']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests:
print(str(len(guests)) + " guests are coming")

# 3-10. Every Function:
places2 = ['japan', 'america', 'gb', 'germany', 'italy']

print(places2)
print(sorted(places2))
print(places2)
print(sorted(places2, reverse=True))
places2.reverse()
places2.reverse()
places2.sort()
places2.sort(reverse=True)

# 3-11. Intentional Error:
# motorcycles = []
# print(motorcycles[-1])

# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

# Making Numerical Lists
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 3)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# Working with Part of a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)


dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

