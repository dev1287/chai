class Car:
#add a class variable to kepp track on cars
    totals_car = 0
#below are attributes (variables)
    #brand = None
    #model = None
# we have to write it __init__ only it a constructor   
    def __init__(self, ubrand, umodel):
    #below are attributes
        self.__brand = ubrand
        self.__model = umodel
        Car.totals_car += 1
#this is encapsulation
    def get_brand(self):
        return self.__brand + " getter!"
#add functinality here like first+lastname , any new functinalty
#if we dont keep self in can access constructor attributes
    def full_name(self):
        return f"{self.__brand} {self.__model}"
 #this is polymorphism one method can be used in many ways (this can also be used in electric)      
    def fuel_type(self):
        return "Petrol or Diesel"
#Add a static method
    @staticmethod
    def general_description():
        return "cars r 4 transport"
#property decarator read only
    @property
    def model(self):
        return self.__model
    

# thi is inheritance
class Electriccar(Car):
    def __init__(self, ubrand, umodel, batterysize):
        super().__init__(ubrand, umodel)
        self.batterysize = batterysize
 #this is polymorphism one method can be used in many ways (this can also be used in electric)   
    def fuel_type(self):
        return "Electric"

class Battery:
    def Battery(self):
        return "batery class" 
    
    
    #pass is used pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

class Engine:
    def Engine(self):
        return "Engine class" 

class ElectricTwo(Battery, Engine, Car):
    pass
 
#below is istance of a car
my_car = Car("toypto","carolla")
#print(my_car.__brand)
print(my_car.get_brand())
#print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())
print("----------------------------------------")
#my_newcar = Car("tata","safari")
#print(my_newcar.model)
#print(my_newcar.full_name())
print("----------------------------------------")
my_tesla = Electriccar("Tesla","Model x","250 KW")
#print(my_tesla.__brand)
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.batterysize)
print(my_tesla.full_name())
print(my_tesla.fuel_type())
print("----------------------------------------")
print(Car.totals_car)

my_hyn = Car("Hyndai","sanafi")
my_hyn.__model = "city"
print(my_hyn.__model)
print(my_hyn.general_description()) #this works if self is given and static method is removed
print(Car.general_description()) 

print("--------------is istance function-------------------------")
my_tesla2 = Electriccar("Tesla","Model x","250 KW")
print(isinstance(my_tesla2, Electriccar))
print(isinstance(my_tesla2, Car))
print("---------------multi inheritance-----------------------")
my_tesla3 = ElectricTwo("Tesla","Model y")

print(my_tesla3.Engine())
print(my_tesla3.Battery())
