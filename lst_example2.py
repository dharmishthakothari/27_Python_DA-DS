lst_numbers = [11,23,32,45,67]
sum=0
countEven=0
countOdd=0
for i in lst_numbers:
    print(i)
    sum=sum+i
    if i%2==0:
        countEven+=1
    else:
        countOdd+=1


print(sum ,"  ",countOdd,"   ",countEven)