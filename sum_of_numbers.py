#Programming Challenge: Sum of Numbers From A Positive Integer
rv = int(input("Enter the positive integer : "))
sum=0
inte = rv 
while rv>0:
    sum+=rv
    rv-=1
    
print(inte)
print("The sum of positve integers to the given number is :",sum)    