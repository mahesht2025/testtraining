# Errors and Exceptions Homework
# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)

except:
    print("Type Error occured!..")        


# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# Handle the exception thrown by the code below by using 
# try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x/y
except:
    print("ZeroDivision Error occured!...")


# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            res=int(input("Enter the Integer Value : "))
        except:
            print("Error occured , Please enter the correct value...")
            continue
        else:
            break

    print("The square of " +str(res) + " is : " ,(res**2))    
ask()