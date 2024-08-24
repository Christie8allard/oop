#class attribute
class Dog(): #capital D makes it an object
    pass
    kind = 'canine'
    breed = 'pug'
    age = 5
    colour = 'black'

# instance attribute - things we want to change
def __init__(self, breed, age, colour, name): #need to have self. included
    self.name = name 
    self.breed = breed
    self.age = age
    self.colour = colour

dog = Dog('jett', 'pug', '5', 'black')
print(dog.name, dog.breed, dog.age, dog.colour)
dog2 = Dog('bub', 'poodle', '3', 'blond')
print(dog2.name, dog2.breed, dog2.age, dog2.colour)

def eat(self):
    print("nom nom nom")
    new_weight = self.weight + 0.5

name = "asli"
name.eat()