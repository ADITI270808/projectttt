class Atm:
    def __init__(self, cardNumber, Pin):
        self.cardNumber = cardNumber
        self.Pin = Pin
    
    def check_balance(self):
     print("balance is 100000")
     
    def withdrawl(self,amount):
        new_amount = 100000 - amount
         print("you have withdrawn amount"+str(amount)+".your remaining balance is" + str(new_amount))


if __name__ == "__main__":
    main()