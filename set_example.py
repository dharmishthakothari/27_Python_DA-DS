lst_numbers = [12,23,34,56,78,12,23]
print(lst_numbers)
# conversion from list to set
st_numbers=set(lst_numbers)
print(st_numbers)
st2={12,23,45,67}
# find diff between 2 sets 
st1=st_numbers.difference(st2)
print(st1)
# find union among 2 sets 
st3=st_numbers.union(st2)
print(st3)
