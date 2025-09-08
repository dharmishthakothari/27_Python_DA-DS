from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def greet(self):
        pass
class Test2(Test):
    def display(self):
        print("in display")
t=Test2()
t.display()