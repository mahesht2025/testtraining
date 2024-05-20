# Functions and Methods Homework
# Complete the following questions: 
# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as
# 43πr3
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
print(vol(2))

# Write a function that checks whether a number is in a given
# range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high):
        print("The "+str(num)  + " number is present in the range")
    else:
        print("The "+ str(num)  + " number is Not present in the range")
# Check
ran_check(5,2,7)

# 5 is in the range between 2 and 7
# If you only wanted to return a boolean:
def ran_bool(num,low,high):
    if num in range(low,high):
        return True
    else:
        return False
print(ran_bool(3,1,10))
True

# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!
s = "Hello Mr. Rogers, how are you this fine Tuesday?"    
def up_low(s):
    f={"up":0, "low":0}
    for c in s:
        if c.isupper():
            f["up"]+=1
        elif c.islower():
            f["low"]+=1
        else:
            pass
    
    print(" String : ", s)
    print("No. of Upper case  : ", f["up"])
    print("No. of Lower case  : ", f["low"])
up_low(s)
# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33

# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    c=[]
    for i in lst:
        if i not in c:
            c.append(i)
    return c        
    
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
[1, 2, 3, 4, 5]
# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):
    res = 1
    for x in numbers:
        res *= x
    return res
print(multiply([1,2,3,-4]))
numbers=[1,2,3,-4]
# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward 
#as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". 
# Hint: You may want to check out the .replace() method in a string to help out 
# with dealing with spaces. Also google search how to reverse a string in Python, 
# there are some clever ways to do it with slicing notation.

def palindrome(s):
    
    s = s.replace(' ','') 
    return s == s[::-1] 
print(palindrome('two'))
# Hard:
# Write a Python function to check whether a string is pangram or not. 
# (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the 
# alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the string module
# Hint: In case you want to use set comparisons

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset 
print(ispangram("The quick brown fox jumps over the lazy dog"))
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'