student_info ={
    "12345":['Khushali','Python',100,'A'],
    "22222":['Nandini','DA',100,'A'],
    "44444":['Priyma','DA',80,'B'],
    "55555":['Bhavesh','DS',90,'A'],
    "99999":['Jay','DA',70,'A'],
}
grade=0
lst_a_student=[]
for i,j in student_info.items():
    #print(i,'----> ',j)
    for k in j:
    
        if k=='A' or k=='a':
            grade+=1
            lst_a_student.append(j[0])

print(grade)
print(lst_a_student)

# find no of A student
# List name of A student