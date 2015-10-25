"""uses inheritance based on item type."""
class StoreItems(object):
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Apparel(StoreItems):
    def __init__(self, name, price, description, sizes, colors):
        self.sizes = sizes
        self.colors = colors
        StoreItems.__init__(self, name, price, description)

class Part(StoreItems):
    def __init__(self, name, price, description, dimensions, make, model):
        self.dimensions = dimensions
        self.make = make
        self.model = model
        StoreItems.__init__(self, name, price, description)
