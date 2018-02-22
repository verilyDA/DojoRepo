# Classes
# declare a class and give it name User
# instantiate class User
class User(object):
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes
        self.name = name
        self.email = email
        self.logged = True
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print (self.name + " is logged in.")
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print (self.name + " is not logged in")
        return self
    # print name and email of the calling instance
    def show(self):
        print ("My name is {}. You can email me at {}".format(self.name, self.email))
        return self

#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print(new_user.email)

#inheritance

#class Parent(object): # inherits from the object class
  # parent methods and attributes here
#class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes


class Vehicle(object):#parent class
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):#child class
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):#child clas
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):#child class
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print (v.make)
b = Bike(2,1,"Schwinn","Paramount")
print (b.vehicle_type())
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print (a.mileage)

#Multiple arguments

def varargs(arg1, *args):
  print ("Got " + arg1 + " and " + ", " .join(args))
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"

def varargs(arg1, *args):
   print ("args is of " + str(type(args)))
varargs("one", "two", "three") # output: args is of <type 'tuple'>

#Super

from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
