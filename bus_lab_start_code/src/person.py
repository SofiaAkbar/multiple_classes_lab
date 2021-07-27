class Person:
    def __init__(self, name, age, cash = 0, destination = ''):
        self.name = name
        self.age = age
        self.cash = cash
        self.destination = destination

    def pay_bus_fare(self, amount):
        self.cash -= amount