# Parent class
class Animal:
    type = "Animal"
    def __init__(self, name, age=0):
        self.name = name
        self.age = 0  # Default age
        self.speak()
        
    def speak(self):
        return "Some generic sound"

# First child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def speak(self):
        return "Woof!"
        
    def fetch(self):
        return f"{self.name} is fetching the ball"

# Second child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def speak(self):
        return "Meow!"
        
    def climb(self):
        return f"{self.name} is climbing a tree"
    
class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def speak(self):
        return "Moo!"
        
    def milk(self):
        return f"{self.name} is being milked"

# Method that accepts parent type as parameter
def identify_animal(animal):
    # Check the actual type of the object
    if isinstance(animal, Dog):
        return f"This is a Dog named {animal.name} (Breed: {animal.breed})"
    elif isinstance(animal, Cat):
        return f"This is a Cat named {animal.name} (Color: {animal.color})"
    elif isinstance(animal, Animal):
        return f"This is a generic Animal named {animal.name}"
    elif isinstance(animal, Cow):
        return f"This is a Cow named {animal.name} (Color: {animal.color})"
    else:
        return "Unknown object type"

Animal.type = "Modified Animal Type"
aa = Animal("Test")
aa.name = "New Name"
print(aa.name)




# Create instances
generic_animal = Animal("Generic")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
cow = Cow("Bessie", "Brown")


# Call the function with different objects
result1 = identify_animal(generic_animal)
result2 = identify_animal(dog)
result3 = identify_animal(cat)
result4 = identify_animal(cow)





# def GetIncommingName(animal):



class Product:
    def __init__(self, name, age=0):
        self.name = name
        self.md = 0  # Default age
        logging.info("Product created")

class Book(Product):
   def __init__(self, name, author):
        super().__init__(name)
        self.author = author





























        