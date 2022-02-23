def pyramid(y):
    # number of spaces
    x = y - 1

    # loop to handle number of rows
    for p in range(0, y):

        # loop to handle number of spaces
        for q in range(0, x):
            print(end=" ")

        # decrementing x after each loop
        x = x - 1

        # loop to handle the number of columns
        for q in range(0, p + 1):
            #Finally,printing the stars
            print("* ", end="")

        # ending and inserting a new line after each row
        print("")

# Main code
y = 5
pyramid(y)