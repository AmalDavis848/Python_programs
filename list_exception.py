'''try:
    my_list=[1,2,3,4,5]
    print(my_list[5])
except IndexError:
    print("error,index is out of range")'''
try:
    def list_exception(list,index):
     print("index :",list[index])
except IndexError:
    print("error")
mylist=(input("enter the no seperated by spaces")).split()
index=int(input("enter the index you want to print"))
print(mylist)

list_exception(mylist,index)


