# Warmup Section:

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
#if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and
#returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    word = text.split()
    if word[0][0] == word[1][0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or 
#if one of the integers is 20.
#If not, return False

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or (n1+n2) == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# LEVEL 1 PROBLEMS

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    A = name[:3].capitalize()
    B = name[3:].capitalize()
    C = A + B
    return C

print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    A = text.split()[::-1]
    return ' '.join(A)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#ALMOST THERE: Given an integer n, return 
#True if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(n):
    A = abs(100 - n)
    B = abs(200 - n)
    if A <= 10 or B <= 10:
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# LEVEL 2 PROBLEMS

#FIND 33:Given a list of ints,
#return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#PAPER DOLL: Given a string, return a string 
#where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    count = ""
    for i in text:
        count += i * 3
    return count

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

#BLACKJACK: Given three integers between 1 and 11, 
#if their sum is less than or equal to 21, 
#return their sum. If their sum exceeds 21 and 
#there's an eleven, reduce the total sum by 10. 
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif sum > 21 and 11 in (a,b,c):
        sum -= 10
        return sum
    elif sum > 21:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#SUMMER OF '69: Return the sum of the numbers in the array,
#except ignore sections of numbers starting with a 6 and
#extending to the next 9 (every 6 will be followed by at least one 9).
#Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    total = 0
    add = True  # This flag indicates whether we should add the numbers to the total or not
    for num in arr:
        if add:
            if num == 6:  # When we encounter a 6, we stop adding to the total
                add = False
            else:
                total += num
        else:
            if num == 9:  # When we encounter a 9, we resume adding to the total
                add = True
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# CHALLENGING PROBLEMS

#SPY GAME: Write a function that takes in a list of integers and 
#returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    code = [0, 0, 7, 'x']

    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# #COUNT PRIMES: Write a function that returns the number of prime numbers
# #that exist up to and including a given number

# # count_primes(100) --> 25

# def count_primes(num):

# print(count_primes(100))

def count_primes(n):
    prime = [2]
    x = 3
    if n < 2:  
        return 0
    while x <= n:
        for y in range(3,x,2):  
            if x%y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    print(prime)
    return len(prime)

count_primes(100)



# Just for fun:
#PRINT BIG: Write a function that takes in a single letter
#and returns a 5x5 representation of that letter

# print_big('a')
# out:   *  
#       * *
#      * * *
#      *   *
#      *   *

def print_pat(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alph = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alph[letter.upper()]:
        print(patterns[pattern])

print_pat('D')