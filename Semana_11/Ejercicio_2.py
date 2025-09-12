class Person:
    def __init__(self, name):
        self.name = name
    

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got on the bus.")
        else:
            print("The bus is full. Cannot add more passengers.")

    def remove_passenger(self, passenger):
        if self.passengers:
            person = self.passengers.pop()
            print(f"{person.name} got off the bus.")
        else:
            print("There are no passengers to remove.")
    
    def print_status(self):
        print(f"Bus has {len(self.passengers)} out of {self.max_passengers} passengers.")

p1 = Person("Anna")
p2 = Person("Luis")
p3 = Person("Sophie")

bus = Bus(2)

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger(p3)

bus.print_status()
bus.remove_passenger(p1) #choose passenger to remove
bus.print_status()