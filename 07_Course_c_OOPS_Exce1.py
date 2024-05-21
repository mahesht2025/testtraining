# Fill in the Line class methods to accept coordinates
#  as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    
    def distance(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2-y1)/(x2-x1)


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance()) #9.433981132056603
print(li.slope()) #1.6
# Problem 2
#Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*3.14*self.radius*self.height) + (2*top)
a = Cylinder(2,3)
print(a.volume()) #56.52
print(a.surface_area()) #94.2



