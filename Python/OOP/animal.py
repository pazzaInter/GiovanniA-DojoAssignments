class Animal(object):
    """docstring for Animal."""
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Name:", self.name
        print "Health:", self.health, "\n"
        return self

cat = Animal('Scrap')

cat.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    """docstring for Dog."""
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health -= 5
        return self

fred = Dog('Fred')

fred.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def display_health(self):
        print "This is a dragon!"
        return super(Dragon, self).display_health()
    def fly(self):
        self.health -= 10
        return self


drogon = Dragon('Drogon')

drogon.walk().walk().walk().run().run().fly().fly().display_health()

fish = Animal('Gold')

fish.display_health()

# uncomment the following to test that a dog cannot fly

# try:
#     fred.pet().display_health().fly()
# except AttributeError:
#     print "Dogs cannot fly"
