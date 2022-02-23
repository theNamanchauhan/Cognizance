# i)
r1=['Roll Number','Name','Marks']
list=[r1]
#No. of enteries/Rows the user want in their Table
entries=int(input("Number of records:- "))
for i in range(entries):
    print('Enter the following details: ','Record no:-',i+1)
    r2 = [input('Enter Roll number:- '),input('Enter Name:- '),input('Enter Marks:- ')]
    r3 =r2
    #Adding the following details in the existing record
    list.append(r3)
print()
for i in list:
    print(i[0]+'    '+i[1]+'    '+i[2])



# ii)
#Now, We are checking record 2 is present or not,accordingly we have to print record 2
if len(list)<3:
    print("Record 2 not found ")
else:
    print("Record 2")
    print(list[2][0]+'  '+list[2][1]+'  '+list[2][2])