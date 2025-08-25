with open("greet.txt","r") as file:
    current_position=file.tell()
    print(f"Before reading content position is {current_position}")
    file.seek(17)
    #file.write("AfterNoon")
    data=file.read()
    print(data)
