"""Question 2:
Define a class named "ItemInfo with the following description:
item_code (Item Code), item (item name), price (Price of each item), 
qty (quantity in stock), discount (Discount percentage on the item), net_price (Price after discount) 

Methods:
• A member method calculate_discount() to calculate discount as per the following rules:
• If qty <= 10 -> discount is 0
• If qty (11 to 20 inclusive) -> discount is 15
• If qty = 20 ->discount is 20 
• A constructor init method to assign the initial values for item_code to and price, qty, net_price and discount to null
• A function called buy() to allow user to enter values for item_code, item, price, qty. 
  Then call function calculate_discount() to calculate the discount and net_price (price* qty - discount). 
• A function show_all() or similar name to allow user to view the content of all the data members."""
import os 
class ItemInfo():

    item_code   = 0
    item        = None
    price       = None
    qty         = None
    def __init__(self, item_code, item, price, qty):
        self.item_code  = item_code
        self.item       = item
        self.price      = price
        self.qty        = qty            
                        
    def calculate_discount(self):
        self.discount   = self.price*self.qty
        if self.qty >= 20 :
            self.discount =self.discount*0.20                                        
        elif 11 <= self.qty < 20 :
            self.discount = self.discount*0.15
        else:
            self.discount = 0
        self.net_price  = self.price*self.qty-self.discount
        return self.discount , self.net_price

    def show_all(self):
        print(  "------------------",
                "ItemCode  : " f"{self.item_code}",
                "ItemName  : " f"{self.item}",             
                "Price     : " f"{self.price}",
                "Quantity  : " f"{self.qty}",
                "Discount  : " f"{self.discount}",
                "NetPrice  : " f"{self.net_price}",
                "------------------",sep=("\n"))

    def buy():
        data = ItemInfo(    input("item_code:"),
                            input("item     :"),   
                            float(input("Price    :")),
                            int(input("qty      :"))
                            )    
        return data

data = ItemInfo.buy()
data.calculate_discount()
os.system('cls||clear')
data.show_all() 
