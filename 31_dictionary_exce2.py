#use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the string "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.  "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of those key: value pairs on a different line.  For example, the first 3 lines in the output should be the following:
for key,value in {}.fromkeys("abcdefghijkl",'consonants').items():
    print(key,value)
