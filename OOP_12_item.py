import csv

class item:
    pay_rate = 0.8
    all = []
    def __init__(self, name:str, price:float, qty=0):
        assert price >= 0, f"price :{price} is less than 0"
        assert qty >= 0 , f"quantity : {qty} is less than 0 "

        self.name = name
        self.price = price
        self.qty = qty

        item.all.append(self)

    @property
    def name(self):
        # Property decorator = read only attribute
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10 :
            raise Exception("The name is too long! ")
        else :
            self.__name = value
        
    def calculate_total_price(self):
        return self.qty * self.price

    def discount_applied(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        f.close()

        for i in items:
            item(name = str(i.get('name')),
                 price = float(i.get('price')),
                 qty = int(i.get('quantity')),)

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.qty}')\n"

    
    
