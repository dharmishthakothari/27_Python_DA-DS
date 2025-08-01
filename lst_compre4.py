lst_city = ['ahmebabad','Baroda','SuRat']
# lst_city_upper=[]
# for i in lst_city:
#     if len(i)>5:
#         lst_city_upper.append(i.upper())

# print(lst_city_upper)

lst_city_upper = [i.upper() for i in lst_city if len(i)>5]
print(lst_city_upper)