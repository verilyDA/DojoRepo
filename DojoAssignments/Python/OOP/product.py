class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        self.price = self.price * ( 1 + tax )
        return self
    def return_item(self, reason):
        if reason == 'defective':
            self.price = 0
            self.status = 'defective'
        if reason == 'closed box':
            self.status = 'for sale'
        if reason == 'open box':
            self.price = self.price * 0.8
            self.status = 'used'
        return self
    def display_info(self):
        print('Item name: ', self.item_name)
        print('Price: ', self.price)
        print('Weight: ', self.weight)
        print('Brand: ', self.brand)
        print('Status: ', self.status)

toy_car = product(50, 'toy car', 4, 'Mattel')
toy_car.display_info()
