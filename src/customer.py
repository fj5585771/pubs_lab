class Customer:
    def __init__(self, name, wallet, age):
        self.name  = name
        self.wallet = wallet
        self.age = age 

#function that allows a customer to pay for a drink and amends the value of their wallet
    def pay_for_drink(self, price):
        self.wallet -= price



        #self, wallet
        #remove drink price from wallet 




        #if the customers wallet is > the price of a drink
        #then give the customer a drink 
        #reduce the size of the customers wallet
        #and reduce the value of the pubs till by the price of a drink