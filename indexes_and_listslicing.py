#Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
man = [[0,2],[4,6],[8,10],[12,14]]

#Access the first list from the list of lists in step 1 by index then print it.
print(man[0])

#Access the 14 from the list in step 1 then print it.
print(man[3][1])

#Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
furn=["chair", "table", "desk", "lamp", "bed"]

#Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(furn[-5])

#Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
print("Most people own at least "+str(man[0][1])+" "+furn[0]+"'s" )