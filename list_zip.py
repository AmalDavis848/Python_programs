list1=[1,2,3]
list2=['a','b','c']
list3=['x','y','z']

zipped_list=zip(list1,list2,list3)
result=list(zipped_list)
print(result)
#print(zipped_list)

unzipped_list=zip(*result)
print(unzipped_list)

unzipped_list=[list(item) for item in unzipped_list]
print(unzipped_list)
    