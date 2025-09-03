# inheritance 
class Person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"This is Person details {self.name} - {self.c_no}",end="\t")
class Employee(Person):
    def __init__(self, name, c_no,dept,salary):
        super().__init__(name, c_no)    
        self.dept=dept
        self.salary=salary
    def display(self):
        super().display()
        print(" - ",self.salary," - ",self.dept)
        #return super().display()
    
pooja=Employee("pooja",98765432,"Analyst",2345676)
pooja.display()
dimple=Person("dimple",6754434)
dimple.display()