from OOP_11_inheritance import item

class phone(item):
    def __init__(self, name:str, price:float, qty=0, broken_phone = 0):
        super().__init__(name, price, qty)

        assert broken_phones >= 0, f"broken_phones = {broken_phones} is less than 0"
        self.broken_phones = broken_phones
