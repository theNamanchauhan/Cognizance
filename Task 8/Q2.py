import numpy as np
#Getting list-1 from user
list1=list(input("Enter First array: "))
#Creating array-1 from user entered list
arr1=np.array(list1)

#Getting list-2 from user
list2=list(input("Enter Second array: "))
#Creating array-2 from user entered list
arr2=np.array(list2)

#Checking whether the Two arrays have same elements or not and printing the result
print(np.array_equal(arr1,arr2))