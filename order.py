import client

class Order(client.Client):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender, total_price, status):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender
        self._total_price = total_price
        self._status = status
       
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

    def total_price(self, total_price):
        self._total_price = total_price

    def status(self, status):
        self._status = status
    

    