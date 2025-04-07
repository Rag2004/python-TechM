def loan_eligibility():
    try:
        age=int(input("Enter your age:"))
        salary=float(input("Enter salary:"))
        credit_score=int(input("Enter your credit score:"))

        if age>21 and age<60:
            if salary>25000:
                if credit_score>700:
                    print("You are eligible for loan")
                else:
                    print("Loan Rejected!! Your credit score is less than 700")
            else:
                print("Loan Rejected!! Your salary doesn't meet required criteria")
        else:
            print("Loan Rejected!! Your age is not between 21 to 60")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    loan_eligibility()                        

