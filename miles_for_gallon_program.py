import random

# It is generating the integer between  10 and 25 to represent gas in the car fueltank
fuel = random.randint(10, 25)

# It is generating the integer between  200 and 400 to represent miles the car can go without refueling
miles = random.randint(200, 400)

# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")

# displaying the number of gallons of fuel  the car fuel tank can hold
print("Th e car's fuel tank can hold " + str(fuel) + " gallons.")

# displaying  the number of miles was car can travel with a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")