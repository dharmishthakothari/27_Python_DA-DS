dict1={
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five"
}
#iterate all key
for i in dict1:
    print(i)
#iterate all values
for i in dict1.values():
    print(i)
#interate both
for i,j in dict1.items():
    print(i,'--->',j)

print(dict1[5])