lst_city = ['ahmebabad','baroda','surat','rajkot']
for i in lst_city:
    
    if len(i)>5 and i.startswith("ahm"):
        print(i.upper()," -->  ",len(i))
print(len(lst_city))

