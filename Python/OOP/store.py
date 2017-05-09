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
        print "\nItem Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        print "Discount:", self.discount, "\n"
        return self

class Store(object):
    """docstring for Store."""
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
        self.num_of_products = len(products)

    def add_product(self, product):
        """Add a product to the stores list of products"""
        self.products.append(product)
        self.num_of_products = len(self.products)
        return self
    def remove_product(self, product):
        """Remove product from the stores list of products"""
        self.products.remove(product)
        self.num_of_products = len(self.products)
        return self
    def inventory(self):
        """Print info about each product in the store and total number of products"""
        print "\nNumber of prodcuts:", self.num_of_products
        for each in self.products:
            each.display_info()
        return self

playstation1 = Product(500, "Playstation", "3 lbs", "Sony", 0)
playstation2 = Product(50, "Playstation 2", "3 lbs", "Sony", 0)
playstation3 = Product(100, "Playstation 3", "6 lbs", "Sony", 25)
playstation4 = Product(300, "Playstation 4", "5 lbs", "Sony", 150)
xbox3 = Product(300, "Xbox One", "6 lbs", "Microsoft", 200)

best_buy = Store([playstation2, playstation3, playstation4], 'Seattle', 'Best Buy')

best_buy.inventory()
best_buy.add_product(xbox3).add_product(playstation1).remove_product(playstation2)
best_buy.inventory()
