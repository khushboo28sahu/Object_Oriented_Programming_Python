class item:
    
    pay_rate = 0.8      # class level attribute
    all =   []          # list to store all the instances
    
    def __init__(self, name:str, price:float, qty = 0):
        
        # assert check the conditions for the attributes
        assert price >=0, print(f"price :{price} is less than 0")
        assert qty >= 0, print(f"qty : {qty} is less than 0")
        
        # assigning the values for  the self
        self.name = name
        self.price = price
        self.qty = qty

        # execute for all the instances
        self.all.append(self)
        
    def cal_total_price(self):
        return self.price*self.qty
    
    def apply_discount(self):
        
        # self.price = self.price*item.pay_rate
        # item.pay_rate, it is taking the value from the class level attribute.
        
        self.price  = self.price*self.pay_rate
        
        # self.pay_rate first search in an instance level value for the pay_rate
        # and then search for the class level value.

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.qty}) \n"
    
        #### __repr__(self)
        # In Python, __repr__ is a special method used to represent a class’s
        # objects as a string. __repr__ is called by the repr() built-in function.
        # You can define your own string representation of your class objects using
        # the __repr__ method.
        
item1 =item("Laptop", 10000, 5)
# item1.apply_discount()
# print(item1.price)

item2 =item("phone", 5000, 8)
# item2.pay_rate  =   0.7
# item2.apply_discount()
# print(item2.price)

item3 = item("cable", 150, 4 )
item4 = item("mouse", 200, 4)
item5 = item("keyboard", 500, 3)
print(item.all)
