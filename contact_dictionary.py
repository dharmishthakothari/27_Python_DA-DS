menu = "1. For adding \n 2. For removing \n 3. For searching \n4. View all \n5. Exit"
choice=0
contact = {}
while choice!=5:
    print(menu)
    choice=int(input("Enter your choice "))
    
    match choice:
        case 1:
                name=input("Enter name ")
                c_no=int(input("Enter contact no  "))
                contact[name]=c_no
                
        case 4:print(contact)
               
       