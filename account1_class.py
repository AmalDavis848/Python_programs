class Account:
    def __init__(self):
        self.balance=0

def deposit(self):
    accno=int(input("enter the account no you want to deposit "))
    cash=int(input("enter the amount you want to deposit "))
    bank=input("enter the bank of benifictiory ")
    self.balance += cash

def withdraw(self):
    accno=int(input("enter the account no for cash withdrawl "))
    cash=int(input("enter the amount you want to withdraw "))
    if cash > self.balance:
        self.balance -=cash
        print(cash,"withdrawed")
    else:
        print("invalid balance")

def balance_enquiry(self):
    print("balance amount:=",self.balance)

obj=Account()


choice=int(input("enter 1 for deposit\n enter 2 for withdraw\nenter 3 for balance_check"))
if choice==1:
    obj.deposit()
elif choice==2:
   obj.withdraw()
elif choice==3:
    obj.balance_enquiry()
else:
    print("INVALID ENTRY")


