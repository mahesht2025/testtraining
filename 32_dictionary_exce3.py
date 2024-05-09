#paste these 2 dictionaries into your file
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}

#use .update() to add the contents of another_one to internet_celebrities.
another ={"Mahesh":"Dream11"}
internet_celebrities.update(another)

#create a variable and assign it a copy of internet_celebrities.
gamers = internet_celebrities.copy()

#use the .clear() method to get rid of the contents of internet celebrities.
internet_celebrities.clear() 
