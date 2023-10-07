import client

class Order(client.Client):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender, total_price, status):
        self.first_name = first_name
        self.last_name = last_name
        self._address = address
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender
        self.total_price = total_price
        self.status = status
    