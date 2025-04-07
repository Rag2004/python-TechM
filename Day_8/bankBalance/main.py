from bank import Bank
def main():
    atm=Bank()

    while True:
        print("Please Select Transaction:")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
    
        choice=input("Enter your choice between 1-4:")
    
        if choice=='1':
            atm.check_balance()
        
        elif choice=='2':
            try:
                amount=float(input("Enter amount to deposit:"))
                atm.deposit(amount)
            except ValueError:
                print("Enter a valid amount")
    
        elif choice=='3':
            try:
                amount=float(input("Enter amount for withdrawal:"))
                atm.withdraw(amount)
            except ValueError:
                print("Enter valid amount")
        elif choice=='4':
            print("Thank you")
            break                    
        else:
            print("enter number between 1-4")

if __name__ == "__main__":
    main()                



    
      