#Create a variable and assign it the string 
ster = "never give up"

#Access the "p" from the variable by index and print() it
print(ster[12])

#Print the slice "give" from the variable
print(ster[6:10])

#Get and print the slice "up" from the variable
print(ster[11:])

#Print the slice "never" from the variable
print(ster[0:5])

#Get the string slice "give up" from the variable and concatenate it with the string "i will ".  Print the resulting string, which should be "i will give up" where the "give up!" part is a slice.
print("i will " + ster[6:])
