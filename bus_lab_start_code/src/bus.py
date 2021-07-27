class Bus:
    def __init__(self, route_number, destination, price, capacity, total = 0):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers = []
        self.total = total

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def remaining_seats(self):
        self.capacity -= self.passenger_count()
        return self.capacity

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.passengers.append(person)
        bus_stop.clear()
        self.capacity -= len(bus_stop.queue)
        
    def payment(self, bus_stop):
        for person in bus_stop.queue:
            person.cash -= self.price
            self.total += self.price

    