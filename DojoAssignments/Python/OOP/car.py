class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def displayAll(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed) + 'mph')
        print("Fuel: " + str(self.fuel))
        print("Mileage: " + str(self.mileage) + 'mpg')
        print("Tax: " + str(self.tax))
        return self

car1 = car(2000, 35, 'Full', 15)
car2 = car(2000, 5, 'Not full', 105)
car3 = car(2000, 15, 'kind of full', 95)
car4 = car(2000, 25, 'full', 25)
car5 = car(2000, 45, 'empty', 25)
car6 = car(20000000, 35, 'empty', 15)

car1.displayAll()
car2.displayAll()
car3.displayAll()
car4.displayAll()
car5.displayAll()
car6.displayAll()
