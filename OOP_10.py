import csv

class item:
    pay_rate = 0.8
    all =[]
    def __init__(self, name:str, price:float, qty:int):
        assert price >= 0 ;f"price : {price} is less than 0"

        self.name = name
        self.price = price
        self.qty = qty

        item.all.append(self)
        
    def calculate_total_price(self):
        return self.price*self.qty

    def discount_price(self):
        self.price = self.price*self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        
        for i in items:
            item( name = i.get('name'),
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
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.qty}')"

## Inheritance
    
class phone(item):
    def __init__(self, name:str, price:float, qty:0, broken_phones = 0):
        super().__init__(name, price, qty)
        assert broken_phones >=0; f"Broken phones:{broken_phones} is less than 0"
        self.broken_phones = broken_phones



phone1 = phone("jscPhonev10", 500, 5, 1) 
print(item.all)
        

    
    
