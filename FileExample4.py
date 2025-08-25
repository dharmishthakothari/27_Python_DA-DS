with open("function_example4.py","r") as file:
    current_position=file.tell()
    print(f"Before reading content position is {current_position}")
    # data=file.read()
    # current_position=file.tell()
    # print(f"After reading all content of file , position is {current_position}")
    data=file.readline()
    current_position = file.tell()
    print(f"After reading one line of file , position is {current_position}")
    data=file.readline()
    current_position = file.tell()
    print(f"After reading one line of file , position is {current_position}")

