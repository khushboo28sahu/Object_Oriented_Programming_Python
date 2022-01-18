class item:
    pay_rate= 0.8       # class level attribute
    def __init__(self, name, price, qty):
        assert qty >=0 , f"qty:{qty} is less than 0"
        assert price >= 0 , f"price;{price} is less than 0"
        # assigning the self instances
        self.name   =   name # instance level attribute's
        self.price  =   price
        self.qty    =   qty
        
    def cal_total_price(self):
        return self.price * self.qty
    
    def cal_discount(self):
        return self.price*item.pay_rate # self.price is an instance level attribute and item.pay_rate is an class level attribute
item1 =item("phone" ,500, 10)
item2 = item("LAptop" , 1000, 80)


print(item.__dict__)    ##__dict__ is A dictionary or other mapping object used to store an object's (writable) attributes.
# above is  for the class level dictionary
print(item1.__dict__)   # for instance level attributes

print("\n\n")
print(item1.cal_total_price())
print(item2.cal_total_price())

print("\n\n")
print(item1.cal_discount())
print(item2.cal_discount())
