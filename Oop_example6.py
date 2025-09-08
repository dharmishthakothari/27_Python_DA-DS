class Person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(self.name,"  ",self.c_no)
class Employee(Person):
    def __init__(self, name, c_no,salary,dept):
        super().__init__(name, c_no)
        self.dept=dept
        self.salary=salary    
    def display(self):
        #return super().display()
        super().display()
        print(self.salary,self.dept)
emp1=Employee("suraj",4454545,6789,'Sales')
emp1.display()