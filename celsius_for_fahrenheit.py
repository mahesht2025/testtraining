#Programming : Celsius to Fahrenheit
celsius = int(input(" enter the value for degrees celsius. "))
 
 
def fahrenheit(cel):
    
    return (18 * cel + 320) / 10
 
print("The Fahrenheit equivalent of  " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")