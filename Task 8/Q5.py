import numpy as np
#1 Addition of two numpy arrays
print("Part-1")
#Creating two arrays '"arr1" and "arr2"
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

#Adding both the arrays and printing the sum
print(arr1+arr2)
print("\n************************************************\n")
#********************************************************************************************

#5 Array ReDimensioning
print("Part-2")

#Creating an array with 20 Enteries
arr3=np.arange(1,21)

#Printing that array
print("Original Array is ",arr3)

#Printing the size of array
print("Size of original array is ",arr3.size)

#Redimensioning the array and printing it
print("ReDimensioned Array is: \n",arr3.reshape(10,2))


