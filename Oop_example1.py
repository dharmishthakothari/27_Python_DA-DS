class Person:
    def getDetails(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"This is Person details {self.name} - {self.c_no}")
pooja=Person()
pooja.getDetails("Pooja",23456)
pooja.display()
dimple=Person()
dimple.getDetails("Dimple",56756)
dimple.display()