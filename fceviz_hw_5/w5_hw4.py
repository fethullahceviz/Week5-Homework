import os
class Customer():

    def __init__(self,name,last_name,customer_id):
        self.name       =name
        self.last_name  =last_name
        self.customer_id=customer_id

    def get_cust_info(self):        
        self.name       =input("Enter Customer Name : ")
        self.last_name  =input("Enter Customer LastName : ")
        self.customer_id=int(input("Enter Customer Id : "))

class Item(Customer): 
    def __init__(self, price = 0, qty = 0, item = "") -> None:
        Customer.get_cust_info(self)
        self.price  = price
        self.qty    = qty
        self.item   = item

    def input_data(self):
        self.items=[]
        self.total_prices=[]
        while True:
            self.item         =input("Enter an item name: ")
            self.items.append(self.item)

            self.price        = float(input("Enter price: "))
            self.qty          = int(input("Enter quantity: "))
            self.total_price  = self.price * self.qty
            self.total_prices.append(self.total_price)

            choice=input("Add to item [Enter] or Quit [Q oder q]")
            if choice==""                   : continue
            elif choice=="Q" or choice=="q" : break
            else                            : print("InputError")
        return self.items, sum(self.total_prices)
                   
    def shopping_card(self):
        return self.items
        
    def calculate_discount(self):
        self.discount=0  
        if sum(self.total_prices) >= 4000           : self.discount=sum(self.total_prices)*0.25
        elif 4000 > sum(self.total_prices) >= 2000  : self.discount=sum(self.total_prices)*0.15
        else                                        : self.discount=sum(self.total_prices)*0.10
        return self.discount
    
    def get_total_amount(self):
        self.price_tobe_paid=sum(self.total_prices)-self.discount 
        return self.price_tobe_paid

    def __str__(self):
        return f"\n\
            Customer FullName: {self.name} {self.last_name}  CustomerId : {self.customer_id} \n\
            ======================================================\n\
            ShoppingResult: \n\
            Items----------> {self.shopping_card()}\n\
            TotalPrice-----> {sum(self.total_prices)}\n\
            Discount-------> {self.calculate_discount()}\n\
            NetPrice-------> {self.get_total_amount()}\n\
            ====================="
            
data = Item()
data.input_data()
os.system("cls")
print(str(data)) 