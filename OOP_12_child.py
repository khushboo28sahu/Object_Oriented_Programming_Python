from OOP_12_item import item

class phone(item):
    pay_rate = 0.5

    def __init__(self, name:str, price:float, qty=0, broken_phones=0):
        # call to super function to have acess to all attribute/ methods
        super().__init__(name, price, qty)

        # run validation to the received attributes
        assert broken_phones >= 0, f"broken phones is less than 0!"

         # assign to self objects
        self.broken_phones = broken_phones
