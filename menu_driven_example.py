# loop for repeating n time dependes user input
while True:
    # Menu
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. For exit...")

    #input values from user
    number1=int(input("Enter first number "))
    number2=int(input("Enter second number "))
    choice=int(input("Enter your choice "))

    # match case as like your if-elif stmt 
    match choice:
        case 1: print("Addition ",number1+number2)    
        case 2: print("Substraction ",number1-number2)    
        case 3: print("Multilicaiton ",number1*number2)    
        case 4: print("Division ",number1/number2)    
        case 5: break
        case _:print("Enter valid choice..")

