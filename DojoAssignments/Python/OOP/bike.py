class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print("Price: " + str(self.price) + '. Max speed: ' + str(self.max_speed) + '. Miles: ' + str(self.miles))
        return self
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        self.miles -= 5
        return self

b1 = Bike(500, 35)
b2 = Bike(450, 25)
b3 = Bike(50, 12)
b1.ride().ride().ride().reverse().displayInfo()
b2.ride().ride().reverse().reverse().displayInfo()
b3.reverse().reverse().reverse().displayInfo()
