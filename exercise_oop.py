# https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-4-class-inheritance

# OOP Exercise 1: Create a Vehicule Class with instance attributes class with max_speed and mileage instance attributes.
class Vehicule:
    max_speed: int
    millage: int

    def funcion_kilometros(self):
        return self.millage* 1.6
    def __init__(self,max_speed,millage):
        self.max_speed=max_speed
        self.millage=millage

        pass
class Bus (Vehicule):
    costo:int
    def __init__(self,max_speed, millage, costo):
        self.costo=costo
        super(Bus, self).__init__(max_speed,millage)
    def funcion_costo (self):
        return self.costo/self.millage
v = Bus(5,41,50)
print(v.funcion_kilometros(),v.funcion_costo())
v2= Vehicule(10,20)
print(v.max_speed,v.millage,v.costo, )

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# OOP Exercise 4: Class Inheritance
# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
