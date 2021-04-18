import time
class Budget:
    def __init__(self, category):
        self.name = category
        self.balance = 0
        self.expenditure = 0
        
    def userOptions(self):
        print(":::::::::: Parrot's_Budget_App.py :::::::::: \n")
        print(":::::::::: Below Is Our Category Menu ::::::::::")
        print("1. Withdraw From Budget\n2. Deposit To Budet\n 3. Check Budget Balance\n 4. Exit\n")
        selectOption = int(input("::::::: Please Select An Option :::::::\n"))
        
        while True:
            if selectOption == 1:
                self.withdraw()
                break
            elif selectOption == 2:
                self.deposit()
                break
            elif selectOption == 3:
                self.accountBalance()
                break
            elif selectOption == 4:
                self.exit()
                break
                            
            else:
                print("Invalid Option Selected, Please Select A Valid Option")
                print(selectOption)
                continue
     
    def withdraw(self):
        amount = int(input(f"({self.name}) How Much Would You Like To Withdraw?? \n "))
        if self.balance >= amount:
            
            if amount >= 100: 
                self.balance -= amount
                self.expenditure += amount
            else:
                print("Note That You Can't Take Less Than €-100")
                exit()
            
        else:
            print("YOu Have Insufficient Funds \n Please Enter A Lesser Amount.....")
            
    def deposit(self):
        amount = int(input(f"({self.name}) HOw much Would YOu Like To Deposit?? \n "))
        self.balance += amount
        print(f"€{amount} added to {self.name}")
        
    def accountBalance(self):
        print(f"{self.name} have €-{self.balance}")
        return self.balance
    
    def exit(self):
            print(":::::::::: Have A Nice Day ::::::::::")  
            
food = Budget("Food")
clothing = Budget("Clothing")
entertainment = Budget("Entertainment")

print(":::::::::: Welcome To Parrot's Python Budget App ::::::::::")
print("")
print("Category List \n 1. Food \n 2. Clothing \n 3. Entertainment \n")
category = int(input("Please Select A Category: "))

while True:
    if category == 1:
        print (f"\n({food.name})")
        food.userOptions()
        break
    elif category == 2:
        print(f"\n({clothing.name})")
        clothing.userOptions()
        break
    elif category == 3:
        print(f"\n({entertainment.name})")
        entertainment.userOptions()
        break               
    else:
        print("Invalid Option Selected")
        print(category)
        
        
