dict1 = {"Gujarat":"Gandhinagar",
         "Maharastra":"Mumbai",
         "Punjab":"Amritsar",
         "Rajasthan":"Jaipur"
         }

dict2={}
for i,j in dict1.items():
    dict2[i]=j.upper()

print(dict2)

dict3 = {j.upper():i for i,j in dict1.items()}

print(dict3)