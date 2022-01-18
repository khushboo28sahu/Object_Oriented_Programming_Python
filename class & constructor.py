class item:
    def __init__(self, name ,price, qty=0):
        self.name   =   name
        self.price  =   price
        self.qty    =   qty
        print(self.qty)
    def cal_total_price(self, x ,y):
        return x*y

item1 = item("phone", 5000,5)
print(item1.cal_total_price(item1.price, item1.qty))

item2 = item("LAptop", 500,10)
print(item2.cal_total_price(item2.price, item2.qty))

