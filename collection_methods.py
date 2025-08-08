lst_names = ['pooja','dharmishtha','khushali']

lst_names.sort(reverse=True)
print(lst_names)
lst_city = ['ahemdbabd','baroda','surat']
#lst_city.sort(key=len)
lst_city.sort()
print(lst_city)
city=lst_city.pop()
print(city)
#print(lst_city)
tpl_number = 11,12,23,456,23,43

print(max(tpl_number))

dict1 = {1:"Dharmishtha",2 : "Kothari",12:"qwert"}

dict1.setdefault(12,"test")
print(dict1)
