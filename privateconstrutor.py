# class Person:
#     def __init__(self, name, age):
#         # This is a parameterized constructor
#         self.name = name
#         self.age = age
#         self.creation_time 
# # Creating object with parameters
# person1 = Person()
# person1.name = "Alice"
# person1.age = 30
# person1.creation_time = "2023-10-01 10:00:00"

# person2 = Person("Bob", 25)
# person3 = Person("Charlie", 35, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (f"Name: {person1.name}, Age: {person1.age}")


class Singleton:
    __instance = None
    __already_logged = False

    def __init__(self):
        if not Singleton.__already_logged:
            print("Creating Singleton instance")
            Singleton.__already_logged = True
        else:
            print("Singleton instance already exists")
            
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

# Usage
# obj1 = Singleton.get_instance()

# obj1 =Singleton()
obj1= Singleton()
existingObject = Singleton.get_instance()

print(obj1)











