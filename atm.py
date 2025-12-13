class ATM:
    def __init__(self,balance=1000):
        self.balance = balance


    def check_balance(self):
        return f"Your Account Balance is ${self.balance}"
    
    def deposite(self, amount):
        self.balance += amount
        return f"deposited ${amount}. Your New Balance is ${self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdraw ${amount}. Your New Balance is ${self.balance}"
        
        else:
            return "insufficient funds. Withdraw failed."



atm = ATM() 

while True:
    print("1. Check balance")
    print("2. deposite")
    print("3. Withdraw")
    print("4. Exit")


    choice = input("Enter Your choice :")

    if choice == '1':
        print(atm.check_balance())
    
    elif choice == '2':
        amount = float(input("Enter the Deposite Amount: "))
        print(atm.deposite(amount))

    elif choice == '3': 
        amount = float(input("Enter Your Withdarw Amount: "))
        print(atm.withdraw(amount))

    elif choice == '4':
        print("Thank You For Using the ATM, Goodbye.")
        break

    else:
        print("Invalid Choice. Please select the valid option")
