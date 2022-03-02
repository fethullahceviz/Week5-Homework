"""Question 3:
Define a class named Product with the following specifications: 

Data members:
product_id - A string to store product.
product_name - A string to store the name of the product. 
product_purchase_price - A decimal to store the cost price of the product. 
product_sale_price - A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative. 

Methods:
• A constructor to intialize all the data members with valid default values.
• A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below:
Margin          Remarks 
-----------------------
<0 (negative)    Loss 
>0 (positive)   Profit 

• A method set_details() to accept values for product_id.product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method. 
• A method get_details() that displays all the data member """
import os
class Product():

    def __init__(self,  product_id, product_name,
                        product_purchase_price,product_sale_price):
        self.P_Id           = product_id
        self.P_Name         = product_name
        self.P_Purchase_P   = product_purchase_price
        self.P_Sale_P       = product_sale_price
        self.Margin         = self.P_Sale_P-self.P_Purchase_P

    def set_remarks(self):
        if self.Margin < 0 :
            self.Remarks="Loss"
        else:
            self.Remarks = "Profit"
        return self.Remarks

    def set_details():        
        data = Product (
                int(input("ProductId : ")),
                input("ProductName : "),
                float(input("ProductPurchasePrice : ")),
                float(input("ProductSalePrice : ")),                                             
                )
        data.set_remarks()
        return data

    def get_details(self):        
        print(
        "ProductId              : " f"{self.P_Id}",
        "ProductName            : " f"{self.P_Name}",
        "ProductPurchasePrice   : " f"{self.P_Purchase_P}",
        "ProductSalePrice       : " f"{self.P_Sale_P}",       
        "Margin                 : " f"{self.Margin}",
        "Remarks                : " f"{self.Remarks}", sep="\n")

data=Product.set_details()
os.system('cls||clear')
data.get_details()