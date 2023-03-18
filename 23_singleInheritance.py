class Vehicle:
    def __init__(self, wheels) -> None:
        self.noOfWheels = wheels

    def show(self):
        return f"Number of wheels: {self.noOfWheels}"


class Car(Vehicle):
    def __init__(self, wheels, model, seats, colour) -> None:
        self.colour = colour
        self.model = model
        self.noOfSeats = seats
        Vehicle.__init__(self, wheels)

    def show(self):
        return f"Number of seats: {self.noOfSeats}\nModel: {self.model}\nColour: {self.colour}\n{Vehicle.show(self)}"


c = Car(4, "Alto 2010", 4, "White")
print(c.show())
