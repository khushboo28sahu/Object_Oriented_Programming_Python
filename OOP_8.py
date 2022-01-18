
import csv

class item:

    pay_rate = 0.8      # class level attribute
    all =   []          # list 
    
    def __init__(self, name:str, price:float, qty:int):
        
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
        
    @classmethod                
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        #print(items)
        for i in items:
            item( name = i.get("name"),
                  price = float(i.get('price')),
                  qty = int(i.get('quantity')))

        # A class method receives the class as an implicit first argument, just
        # like an instance method receives the instance
        # A class method is a method that is bound to the class and not the
        # object of the class.
        # They have the access to the state of the class as it takes a class
        # parameter that points to the class and not the object instance.
        # It can modify a class state that would apply across all the instances
        # of the class. For example, it can modify a class variable that will be
        # applicable to all the instances.

        
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else :
            return False
       # A static method is also a method that is bound to the class and not
       # the object of the class.
       # A static method can’t access or modify the class state.
       # It is present in a class because it makes sense for the method to be
       # present in class.
    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.qty}) \n"
    
    #### __repr__(self)
    # In Python, __repr__ is a special method used to represent a class’s
    # objects as a string. __repr__ is called by the repr() built-in function.
    # You can define your own string representation of your class objects using
    # the __repr__ method.


 # creating a csv file   
##list1    =   [["name", "price", "quantity"],["Laptop", 10000, 5],["phone", 5000, 8],["cable", 150, 4 ],["mouse", 200, 4],["keyboard", 500, 3]]
##
##with open('data.csv', 'w', newline = '') as file:
##    writer = csv.writer(file)
##    writer.writerows(list1)
##file.close()

item.instantiate_from_csv()
#print(item.is_integer(7.5))


##item1 = item("Laptop", 10000, 5)
##item2 = item("phone", 5000, 8)
##item3 = item("cable", 150, 4 )
##item4 = item("mouse", 200, 4)
##item5 = item("keyboard", 500, 3)



## creating a csv file 
## list    =   []
## for i in range(1,6):
##     list.append([(vars()['item'+str(i)]).name, (vars()['item'+str(i)]).price, (vars()['item'+str(i)].qty)])
##
## print(list)

##Python vars() function returns __dict__ attribute for a module, class,
##instance, or any other object with a __dict__ attribute. So the output of vars
##() function is a dictionary.
#print(item.all)

