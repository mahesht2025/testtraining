#Factorial program
def factorial(num):
    rt =1
    
    for item in range(num,1,-1):
        rt*=item
        
        
    return rt
print(factorial(6))
print(factorial(5))              