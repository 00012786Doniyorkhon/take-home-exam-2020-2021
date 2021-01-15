
## Functional programming elements in python

##### map()

# declare an array
names = ['Dmitriy', 'Stepan', 'Vova', 'Alisher']

# Map array elements with another representation and return an iterator
greeted_names = map(lambda x: 'Hi ' + x, names)

# We can print all names in a for loop
for name in greeted_names:
    print(name)



##### filter()

# declare an array
nums = [13, 4, 18, 35]

# filter only numbers divisible by 5
divisible_by_5 = filter(lambda num: num % 5 == 0, nums)

# Convert the iterator into a list
print(list(divisible_by_5))



## Object-oriented programming elements in python

##### declare a class type - Vehicle with 3 properties: name, max speed and mileage
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

##### creation of object of that Vehicle class
gentra = Vehicle("Lacetti Gentra", 180, 18)

##### usage of the object created
print(gentra.name, gentra.max_speed, gentra.mileage)

