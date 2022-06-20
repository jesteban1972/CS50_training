class Flight():
    def __init__(self, capacity): # constructor: creates new flight with given capacity
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name): # method to add a passenger to the flight
        if not self.getOpenSeats():
            return False
        self.passengers.append(name)
        return True

    def getOpenSeats(self): # method to return number of open seats
        return self.capacity - len(self.passengers)
