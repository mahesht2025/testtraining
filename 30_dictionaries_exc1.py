#create a variable and assign it the following dictionary:
songs_name={"Queen": "Bohemian Rhapsody",
     "Bee Gees": "Stayin' Alive",
     "U2": "One",
     "Michael Jackson": "Billie Jean",
     "The Beatles": "Hey Jude",
     "Bob Dylan": "Like A Rolling Stone"}
#make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

#print the length of the dictionary.
print(len(songs_name))

#use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines
for key in songs_name.keys():
    print(key)

#print all of the values from the dictionary using the .values() method.
print(songs_name.values()) 

#use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key,value in songs_name.items():
    print(key,value)
    
#    use the .get() method to check the dictionary for the key
print(songs_name.get("Promise of the Real","the Promise of the Real is not found in the dictionary"))