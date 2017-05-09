class Product(object):
    """docstring for Product."""
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.discount = 1.00

    def sell(self):
        """changes status to 'sold'"""
        self.status = "sold"
        return self
    def add_tax(self, tax):
        """takes tax as a decimal amount as a parameter and returns the price of the item including sales tax"""
        tax += 1.00
        return self.price * tax * self.discount
    def returns(self, reason):
        """takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount."""
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "unopened":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.discount -= .2
        return self
    def display_info(self):
        """show all product details."""
        print "Item Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        print "Discount:", self.discount, "\n"
        return self

apple = Product(.5, "Apple", "5oz.", "Granny Smith", .2)
apple.display_info()
print apple.add_tax(.08)
