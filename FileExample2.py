# file = open("C:\\Users\\Admin\\Documents\\New folder\\greet.txt","r")
file = open("function_example4.py","r")

# read all content
#data=file.read()

# read content as per size 
#data=file.read(50)

#reading single line at a tile
# data=file.readline()
# print(data)
# data=file.readline()
# print(data)
# data=file.readline()
# print(data)


lst=file.readlines()
print(lst)

