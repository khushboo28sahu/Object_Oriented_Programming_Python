class item:
    
    pay_rate = 0.8
    
    def __init__(self, name:str, price:float, qty = 0):
        
        # assert check the conditions for the attributes
        assert price >=0, print(f"price :{price} is less than 0")
        assert qty >= 0, print(f"qty : {qty} is less than 0")
        
        # assigning the values for  the self
        self.name = name
        self.price = price
        self.qty = qty
        

    def cal_total_price(self):
        return self.price*self.qty
    
    def apply_discount(self):
        
        ## self.price = self.price*item.pay_rate
        ### item.pay_rate, it is taking the value from the class level attribute.
        
        self.price  = self.price*self.pay_rate
        # self.pay_rate first search in an instance level value for  the pay_rate and then search for the class level value.

item1 =item("Laptop", 10000, 5)
item1.apply_discount()
print(item1.price)

item2 =item("phone", 5000, 8)
item2.pay_rate  =   0.7
item2.apply_discount()
print(item2.price)

