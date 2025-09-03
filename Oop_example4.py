# Polymorphisum Operator Overloading
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #def display(self):
    def __str__(self):
        return f"{self.x} : {self.y}"    

        
p1=Point(12,11)
p2=Point(2,3)
#p1.display()
#p2.display()
#p3=p1+p2
print(p1)
print(p2)