class ClinicAppointment:

    def bookAppointment(self,dr_dict):
        self.dr_dict=dr_dict
        name=input("Enter name")
        age=int(input("Enter age "))
        c_no=int(input("Enter contact number "))
        key=dr_dict.keys()
        
        for i in key:
            print(i,dr_dict[i].keys())
        dr_name = input("Please enter dr name ")
        #print(name,age,c_no,dr_name)
        print(dr_dict[dr_name])
        slot=input("Please enter availalbe slots ")
        if self.checkDrAvailibity(dr_dict,dr_name,slot):
            print("Your slot is booked ")
        else:
            print("Please select another slot ")

    def view_Cancle_app(self):
        pass
    def checkDrAvailibity(self,dr_dict,dr_name,slot):
        print("Before ",dr_dict)
        value=dr_dict[dr_name][slot]
        if value<3:
            dr_dict[dr_name][slot]+=1
            return 1
        else:
            return 0

        

        

dr_dict = {
'Dr Shah':{'10 am':0,'11 am':0,'2 pm':0},
'Dr Patel':{'11 am':0 , '3 pm':0 },
'Dr Modi' : {'10 am':0,'11 am':0,'4 pm':0}
}
obj=ClinicAppointment()
while True:
    obj.bookAppointment(dr_dict)
    ch=input("You want to add more appointes (Yes-No) ")
    if ch=='No':
        break
