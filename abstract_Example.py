from abc import ABC,abstractmethod
class RBI(ABC):
    def greet():
        print("Hello ")
    @abstractmethod
    def calculateInterest(self,amount):
        pass
class SBI(RBI):
    def calculateInterest(self,amount):
        # .10 
        return amount+(amount*0.10)
class ICICI(RBI):
    def calculateInterest(self, amount):
        # 0.20
        return amount+(amount*0.20)
class HDFC(RBI):
    pass  
objSbi=SBI()
print(f"SBI = {objSbi.calculateInterest(1000)}")
objIcici=ICICI()
print(f"ICICI = {objIcici.calculateInterest(1000)}")
objHdfc=HDFC()
