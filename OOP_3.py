class item:
    def __init__(self, name=str ,price=float, qty=0):   # asssigning the attribute type's explicitly
        assert qty >= 0 ; f"qty={qty} is not less than or equal to 0"
        assert price >= 0 ;f"price:{price} is not less than or equal to 0"        ## Assertion is a statement to validate the attributes 


        # Assigning the values to the self attribute
        self.name   =   name
        self.price  =   price
        self.qty    =   qty
    def cal_total_price(self):
        return self.price*self.qty

item1 = item("phone", 5000,5)
print(item1.cal_total_price())

item2 = item("LAptop", 500,10)    ## while passing th price values as string, it giving 10 times 500 
print(item2.cal_total_price())
