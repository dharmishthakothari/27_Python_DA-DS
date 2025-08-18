def check(n):
    if n%2==0:
        return n
lst_number=[1,2,6,4,89,23,24]
lst=list(filter(check,lst_number))
print(lst)
# lst1=[]
# for i in lst_number:
#     lst1.append(check(i))
# print(lst1)
    