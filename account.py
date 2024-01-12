balance=0
def deposit():
    accno=int(input("enter the account no you want to deposit "))
    cash=int(input("enter the amount you want to deposit "))
    bank=input("enter the bank of benifictiory ")
    am=balance+cash
    print(cash, "deposited")

def withdraw():
    accno=int(input("enter the account no for cash withdrawl "))
    cash=int(input("enter the amount you want to withdraw "))
    if balance > cash:
       am=balance-cash
    print(cash, "withdrawed ")

def balance_check():
    print("balance amount:",balance)

choice=int(input("enter 1 for deposit\n enter 2 for withdraw\nenter 3 for balance_check"))
if choice==1:
    deposit()
elif choice==2:
    withdraw()
elif choice==3:
    balance_check()
else:
    print("INVALID ENTRY")