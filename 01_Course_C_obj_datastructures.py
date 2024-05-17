#Write an equation that uses multiplication, division, an exponent, addition, 
#and subtraction that is equal to 100.25.
print((191 + (5 **2 ) / 4 * 7) - 134.50)

# What is the value of the expression 4 * (6 + 5)
print(4*(6+5)) # o/p:24
# What is the value of the expression 4 * 6 + 5 
print(4 * 6 + 5) # o/p:29
# What is the value of the expression 4 + 6 * 5 
print(4 + 6 * 5) # o/p:34

#What would you use to find a number’s square root, as well as its square?
print(50**0.5) #square root o/p :7.071067
print(5**2) #Square o/p :25

#Strings
# Given the string 'hello' give an index command that returns 'e'.
# Enter your code in the cell below:
strg = "Hello"
print(strg[1])

#Reverse the string 'hello' using slicing:
print(strg[::-1])

#Given the string 'hello', give two methods of producing the letter 'o' using indexing.
print(strg[4])
print(strg[-1])

#Lists
#Build this list [0,0,0] two separate ways.
list1 =[0,0,0]
print(list1)
print([0]*3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list2 = [1,2,[3,4,'hello']]
list2[2][2]="goodbye"
print(list2)

#Sort the list below:
list3 = [50,30,40,60,1]
print(sorted(list3))
list3.sort()
print(list3)

#Dictionaries
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Tuples
#How do you create a tuple?
s=(1,2,3)

#Set
#Use a set to find the unique values of the list below:
temp =[1,4,2,7,6,5,6,9,3,3,2,1]
print(set(temp))

#Booleans
# What will be the resulting Boolean of the following pieces of code 
# (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
print(2>3)
# Answer before running cell
3 <= 2
print(3 <= 2)
# Answer before running cell
3 == 2.0
print(3 == 2.0)
# Answer before running cell
3.0 == 3
print(3.0 == 3)
# Answer before running cell
4**0.5 != 2
print(4**0.5 != 2)
