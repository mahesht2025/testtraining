# Built-in Functions Test
# For this test, you should use built-in functions and be able to write the requested functions in one line.
# Problem 1
# Use map() to create a function which finds the length of each word in
# the phrase (broken by spaces) and returns the values in a list.

# The function will have an input of a string, and output a list of integers.

def word_lengths(phrase):
    
    return list(map(len, phrase.split()))
print(word_lengths('How long are the words in this phrase'))

# Problem 2
# Use reduce() to take a list of digits and return the number that they correspond to.
# For example, [1, 2, 3] corresponds to one-hundred-twenty-three.
# Do not convert the integers to strings!

from functools import reduce

def digits_to_num(digits):
    
    return reduce(lambda a,b:a*10 + b,digits)
print(digits_to_num([3,4,3,2,1]))

# Problem 3
# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):
    
    return list(filter(lambda word:word[0]==letter,word_list))
t = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(t,'h'))
# Problem 4
# Use zip() and a list comprehension to return a list of the same length where
# each value is the two strings from L1 and L2 concatenated together with
# connector between them. Look at the example output below:

def concatenate(L1, L2, connector):
    
     return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
print(concatenate(['A','B'],['a','b'],'-'))

# Problem 5
# Use enumerate() and other skills to return a dictionary which has the 
# values of the list as keys and the index as the value. You may assume that a 
# value will only appear once in the given list.

def d_list(L):
    
    return {key:value for value,key in enumerate(L)}
print(d_list(['a','b','c']))

# Problem 6
# Use enumerate() and other skills from above to return the count of the number
# of items in the list whose value equals its index.

def count_match_index(L):
    
     return len([num for count,num in enumerate(L) if num==count])
print(count_match_index([0,2,2,1,5,5,6,10]))