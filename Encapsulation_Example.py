class Test:
    def greet1(self):
        print("Good Morning ")
    def _greet2(self):
        print("Have a nice day ")
    def __greet3(self):
        print(" Bye ")
class Test1(Test):
    pass
t1=Test()
t1.greet1()
t1._greet2()
#t1.__greet3()
print("From child class")
t2=Test1()
t2.greet1()
t2._greet2()
t2.__greet3()
