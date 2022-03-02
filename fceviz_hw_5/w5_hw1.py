"""Question 1: 

Create the class Society with following information: 
society_name, house_no_of_mem, flat, income 

Methods: 
* An __init_ method to assign initial values of society_name, house_no_of_mem, flat, income 
* input_data() To read information from members 
* allocate_flat() To allocate flat according to income using the below table. 
* show_data() to display the details of the entire class.

Incom                   Flat
------------------------------
>= 25000                A Type
>=20000 and <25000      B Type
>=15000 and <20000      C Type
<1500                   D Type"""
import os
class Society():

    def __init__(self,society_name,house_no_of_mem,flat,income):
        self.s  = society_name
        self.h  = house_no_of_mem
        self.i  = income
        self.f  = flat

    def inputData():
        data = Society (    input("Enter Society Name :"),      
                            int(input("Enter House Number :")),
                            input("Enter a Flat :"),
                            float(input("income :")))                    
        return data

    def allocate_flat(self):        
        if self.i>=25000:
            self.f ="AType"           
            
        elif self.i>=20000 and self.i<25000:
            self.f ="BType"
           
        elif self.i>=15000 and self.i<20000:
            self.f = "CType"
           
        else:
            self.f = "DType"
        return self.f

    def show_data(self):
        
        print(  "SocietyName     : " f"{self.s}",
                "HouseNoOfMember : " f"{self.h}",             
                "Flat            : " f"{self.f}",
                "Income          : " f"{self.i}", sep=("\n"))
                
data = Society.inputData()
data.allocate_flat()
os.system('cls||clear')
data.show_data() 
