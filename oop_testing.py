class Dog:
    def __init__(self):
        pass

    def pet_info(self, age, color):
        self._age = age
        self._color = color

    def display_info(self):
        print("Age: {self._age}, Color: {self._color}")
    
    def bark(self):
        print("ruff ruuff...arf")

    def eat(self):
        print("OM NOM NOM NOM")
    
    def sleep(self):
        print("zzzZZZZ")
        
george = Dog()
george.bark()