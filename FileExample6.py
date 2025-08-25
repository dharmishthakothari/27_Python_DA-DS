import json
data ={
    "id":101,
    "name":"Dimple",
    "marks":120,
    "address":"C G Road",
    "subject":['Excel','SQL','Python']

}

with open("studentData.json","w") as file:
    json.dump(data,file)
