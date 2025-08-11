def personDetail(**pooja):
    print(pooja)
    for k,v in pooja.items():
        if k=="name":
            print(v.upper())


personDetail(name="Dharmishtha",age=30)
personDetail(name="Pooja ",age=20,address="Parimal ",subject="Python")
