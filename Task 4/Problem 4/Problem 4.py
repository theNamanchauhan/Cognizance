#Getting the number from user
s=input("Enter the number: ")

'''However, if we dont do typecasting to convert s into integer then this program can also be used
to check palindrome words as well'''

#Reversing the entered number and storing it in r.
r=s[::-1]

if s==r:
    print("True i.e. Entered number is a palindrome number")
elif s!=r:
    print("False i.e. Entered number is not a palindrome number")