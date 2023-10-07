class Client():
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender

    def first_name(self, first_name):
        self._first_name = first_name
    
    def last_name(self, last_name):
        self._last_name = last_name

    def address(self, address):
        self._address = address

    def cell_phone(self, cell_phone):
        self._cell_phone = cell_phone

    def email(self, email):
        self._email = email
    
    def gender(self, gender):
        self._gender = gender
    