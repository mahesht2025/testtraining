#For this challenge, you will be writing a program which uses a for loop to reverse a string. 
strg = input("Please enter a string:")
reverse = ""
 
for item in range(len(strg) - 1, -1,-1):
    reverse += strg[item]
 
print(reverse)