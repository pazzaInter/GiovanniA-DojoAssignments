class Bike(object):
    """docstring for Bike."""
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        """display the bike's price, maximum speed, and the total miles"""
        print "Price:", self.price
        print "Max speed:", self.max_speed
        print "Total miles ridden:", self.miles, "\n"
        return self
    def ride(self):
        """display "Riding" on the screen and increase the total miles ridden by 10"""
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        """display "Reversing" on the screen and decrease the total miles ridden by 5..."""
        print "Reversing"

        #if there are no miles on the bike then we will not go below that
        if self.miles > 0:
            self.miles -= 5
        return self

bike1 = Bike(200, "50mph")
bike2 = Bike(75, "10mph")
bike3 = Bike(50, "5mph")

print 'Bike 1'
for each in range(3):
    bike1.ride()

bike1.reverse()
bike1.displayInfo()

print 'Bike 2'
for each in range(3):
    bike2.ride()
    bike2.reverse()

bike2.displayInfo()


print 'Bike 3'
for each in range(3):
    bike3.reverse()

bike3.displayInfo()
