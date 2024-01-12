class Bank:
    def getroi(self):
        return 10
class Sbi(Bank):
    def getroi(self):
        return 7
class Icic(Bank):
    def getroi(self):
        return 8
b1=Bank()
b2=Sbi()
b3=Icic()
print("Bank rate of interest: ",b1.getroi())

print("Sbi rate of interest: ",b2.getroi())

print("Icic rate of interest: ",b3.getroi())