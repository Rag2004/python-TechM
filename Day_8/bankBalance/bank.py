class Bank:
    def __init__(self,initial_balance=1000):
        self.balance=initial_balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'₹{amount} deposited successfully!')
            self.check_balance()
        else:
            print("Invalid deposit amount")    

    def withdraw(self,amount):
        if(amount<=0):
            print("invalid amount")
        elif(amount>self.balance):
            print(f"Insufficient balance: available balance:₹{self.balance}")
        else:
            self.balance-=amount
            print(f" ₹{amount} withdrawn successfully")
            self.check_balance()
            


        