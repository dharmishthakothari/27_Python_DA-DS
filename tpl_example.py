#add squre of items from tuple to list
tpl_numbers = (2,23,45,67)
print(type(tpl_numbers))
lst_sq_number =[]
lst_sq_number=(i*i for i in tpl_numbers)
lst1=list(lst_sq_number)
print(lst1)


# for i in tpl_numbers:
#     lst_sq_number.append(i*i)
# print(lst_sq_number)

tpl_city = ('ahmebabd','Mumbai')
lt_city=[]
