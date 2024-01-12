try:
    num=int(input("enter the no"))
    if num==0:
         print("factorial of 1 is 1")

         f=1
    for i in range(num,1,-1):
        f=f*i
    print("factoria of num:",f)
except:
    if num<0:
        raise Exception("no factorial for negative nos")