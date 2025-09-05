# Polymorphisum Operator Overloading
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    #def display(self):
    def __str__(self):
        return f"{self.x} : {self.y}"    
    def __add__(self,other):
        p3= Point(self.x+other.x,self.y+other.y)
        return p3        
p1=Point(12,11)
p2=Point(28,3)
p3=Point()
#p1.display()
#p2.display()
p3=p1+p2
print(f"Addition of {p1} , {p2} is {p3}")