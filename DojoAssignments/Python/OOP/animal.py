class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print('Health: ', self.health)
ani = animal('animal', 20)
ani.walk().walk().walk().run().run().display_health()

class dog(animal):
    def __init__(self, name, health = 150):
        super().__init__(name, health)
    def pet(self):
        self.health += 5
        return self

doge = dog('sparky')
doge.walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
    def __init__(self, name, health = 170):
        super().__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super().display_health()
        print('I am Dragon')
        return self

try:
    ani.pet()
except Exception as e:
    print('pet command fail')

try:
    ani.fly()
except Exception as e:
    print('fly command fail')

ani.display_health()
