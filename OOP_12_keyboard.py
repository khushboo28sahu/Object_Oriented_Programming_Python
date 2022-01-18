from OOP_12_item import item

class keyboard(item):
    pay_rate = 0.7
    def __init__(self, name:str, price:float, qty=0):
        super().__init__(name, price, qty)
