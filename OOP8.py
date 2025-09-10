class Person:
    def __init__(self,name,c_no):
        self.name=name
        self.__c_no=c_no
        
    def __str__(self):
        return f"{self.name} - {self._c_no}"
    def getCNo(self):
        return self._c_no
    def setCNo(self,c_no):
        self._c_no=c_no
p1=Person('Dharmihstha')

p1.setCNo(232323)
print(p1.getCNo())
print(p1)
