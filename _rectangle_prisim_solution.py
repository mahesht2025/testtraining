length = int(input("Enter a number for length "))
width = int(input("Enter a number for width :"))
height = int(input("Enter a number for height :"))
 
def vol_of_prisim(length, wwidth, height):
    return length * width * height
 
 
print("The volume of the rectangular prism is " + str(vol_of_prisim(length, width, height)) + " feet.")
