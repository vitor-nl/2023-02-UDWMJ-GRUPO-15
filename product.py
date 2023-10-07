class Product:
    def __init__(self, name, description, price):
        self._name = name
        self._description = description
        self._price = price

    def name(self, name):
        self._name = name
    
    def description(self, description):
        self._description = description
    
    def price(self, price):
        self._price = price