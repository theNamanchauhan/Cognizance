import numpy as np

#Getting input from user
u1=int(input("Enter First number: "))
u2=int(input("Enter Second number: "))
#Creating an array "a"
a=np.arange(u1,u2+1)
arr1 = np.array(a)
print("Original Array is ",a)

#Inserting zero between the elements of the array
x= np.zeros([len(arr1)+(len(arr1-1)*4)])
x[::6]=arr1

#Printing final array
print(x)
