class Person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"This is Person details {self.name} - {self.c_no}")
pooja=Person("pooja",98765432)
pooja.display()
dimple=Person("dimple",6754434)
dimple.display()