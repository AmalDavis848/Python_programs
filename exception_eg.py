try:
    num=int(input("enter the no"))
    if (num<0):
        pass
except:
    print("negative no is invalid")       
f=1
for i in range(num,1,-1):
    f=f*i
print(f)