import random
i=random.randint(10,20)
while True:
    number=int(input("Enter number "))
    if number==i:
        print("You gussed correct number ")
        break
    else:
        print("Try Again")
