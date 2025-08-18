def squ(num):
    return num*num

lst_num=[1,25,657,78,98,3,5,7]
# lst_squ=[]
# for i in lst_num:
#     lst_squ.append(squ(i))
# print(lst_squ)
lst_squ=list(map(squ,lst_num))
print(lst_squ)
lst_qu=list(map(lambda x:x**3,[2,3,4]))
print(lst_qu)