import product, order

class orderitem(product, order):
    def __init__(self, quantity, unitary_price):
        self.quantity = quantity
        self.unitary_price = unitary_price