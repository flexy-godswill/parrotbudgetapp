import time
class Budget:
    def __init__(self, category):
        self.name = category
        self.balance = 7000
        self.expenditure = 0
        
    def userOptions(self):
        print(":::::::::: Parrot's_Budget_App.py :::::::::: \n")
        print(":::::::::: Below Is Our Category Menu ::::::::::")
        print("1. Withdraw From Budget\n2. Deposit To Budget\n3. Check Budget Balance\n4. Exit\n")
        selectOption = int(input("::::::: Please Select An Option :::::::\n"))
        
        while True:
            if selectOption == 1:
                time.sleep(3)
                self.withdraw()
                break
            elif selectOption == 2:
                time.sleep(3)
                self.deposit()
                break
            elif selectOption == 3:
                time.sleep(3)
                self.accountBalance()
                break
            elif selectOption == 4:
                time.sleep(3)
                self.exit()
                break
                            
            else:
                print("Invalid Option Selected, Please Select A Valid Option")
                print(selectOption)
                continue
     
    def withdraw(self):
        withdrew = int(input("How Much Would You Like TO Withdraw??\n"))
        if (withdrew < self.balance):
            amt = self.balance - withdrew
            print("You Have Successfully Withdrew %s From Your Account" %withdrew)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("Your Current Balance is %s" %amt)
            self.done()
        elif (withdrew > self.balance):
            print("Your Balance Is Too Low For The Amount You Want To Withdraw \n Please Try To Withdraw Lesser Than Your Balance")
            time.sleep(3)
            self.withdraw()
            
    def deposit(self):
        amount = int(input(f"({self.name}) HOw much Would YOu Like To Deposit?? \n "))
        self.balance += amount
        print(f"€{amount} added to {self.name}")
        total = amount + self.balance
        print("Your Current Budget Balance Is %s" %total)
        self.done()
        
        
    def accountBalance(self):
        print(f"{self.name} have {self.balance}")
        print(self.balance)
        self.done()
    
    def exit(self):
            print(":::::::::: Have A Nice Day ::::::::::")
    
    def done(self):
        silkydaisy = int(input("Would You Like To Do Something Else?? \n1. Yes \n2.No \n"))
        if(silkydaisy == 1):
            self.userOptions()
        elif (silkydaisy == 2):
            self.exit()
        else:
            print("You Have Selected An Invalid Option, Please Try Again")
            self.done()
              
            
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
        
        
