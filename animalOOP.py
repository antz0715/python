class Animal:
    def __init__(self, name, sound):
        self.name = name  # Attribute: name of the animal
        self.sound = sound  # Attribute: sound the animal makes

    def make_sound(self):
        print(f"A {self.name} goes {self.sound}!") #string concatination

# Creating objects (instances of the Animal class)
lion = Animal("lion", "roar")
monkey = Animal("monkey", "ooh ooh ah ah")
elephant = Animal("elephant", "brrrrr")
cat = Animal("cat", "MEOW")
dog = Animal("dog", "woof")
fish = Animal("fish","bloop - bloop")


# Using methods of the objects
lion.make_sound()
monkey.make_sound()
elephant.make_sound()
cat.make_sound()
dog.make_sound()
fish.make_sound()
