import category

class Product(category.Category):
    def __init__(self, name, description, date_fabrication, is_active = True):
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active

    def name(self, name):
        self.name = name
    
    def description(self, description):
        self.description = description
    
    def date_fabrication(self, date_fabrication):
        self._date_fabrication = date_fabrication

    def deactivated(self):
        if self._is_active:
            print('Product already active.')
        else:
            is_active = False
            print('Deactivated.')