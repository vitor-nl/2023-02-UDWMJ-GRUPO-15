import category

class Product(category.Category):
    def __init__(self, name, description, date_fabrication, is_active = True):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self._is_active = is_active

    def deactivated(self):
        if self._is_active:
            print('Product already active.')
        else:
            is_active = False
            print('Deactivated.')