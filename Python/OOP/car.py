class Car(object):
    """docstring for Car."""
    def __init__(self, car, price, speed, fuel, mileage):
        self.name = car
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12

        # once all attributes have been set we will call display_all
        self.display_all()

    def display_all(self):
        print "Car:", self.name
        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage, "mpg"
        print "Tax:", self.tax, "\n"
        return self

car1 = Car("Toyota", 5000, 50, 'Empty', 30)
car2 = Car("Benz", 500000, 220, 'Full', 15)
car3 = Car("BMW", 50000, 120, 'Empty', 20)
car4 = Car("Ford", 25000, 45, 'Half Full', 10)
car5 = Car("Audi", 55000, 125, 'Empty', 25)
car6 = Car("Ford", 15000, 45, 'Empty', 20)
