#json


import json 

sample={
    "name" : "batman",
    "age" : 45,
    "badhabits" : None,
    "address" : [
        {
            "type" : "home",
            "pincode" : 1
        }
        ],
    "married" : False
}
print (sample)
print(type(sample))

data=json.dumps(sample)     #converts the python format to the string 

print (data)
print (type(data))

original=json.loads(data)       #converts the string to python code
print (original)
print (type(original))
