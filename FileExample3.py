# to Write into file

with open("C:\\Users\\Admin\\Documents\\New folder\\greet.txt","a") as file:
    file.write("Good Morning Have a Nice day!!")
    lst_msg=['Hello ','Friends\n\n','Have ', 'Nice ',' Day']
    file.writelines(lst_msg)
    file.close()