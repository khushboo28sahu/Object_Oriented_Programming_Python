class item:
    def __init__(self, name ,price, qty=0):
        self.name   =   name
        self.price  =   price
        self.qty    =   qty
    def cal_total_price(self):
        return self.price*self.qty

item1 = item("phone", 5000,5)
print(item1.cal_total_price())

item2 = item("LAptop", "500",10)    ## its giving 10 times 500 
print(item2.cal_total_price())

