# replce /replace with count and find
name = "Tops Technologies"
new_name=name.replace("o","*")
print(f"{name} is replaced with {new_name}")
new_name=name.replace("o","*",2)
print(f"{name} is replaced with {new_name}")

index=name.find("Z")
print(index)

ans=name.startswith("T")
print(ans)

msg="Have a great Day!!!"
ans=msg.split(maxsplit=1)
print(ans)
lst=['This','is','python','class']
lst_ans=" ".join(lst)
print(lst_ans)
