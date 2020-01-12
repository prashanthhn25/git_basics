dict_a={
        "name" : "batman",
        "age" : 40,
        "place" : "gotham"
        }
print  (dict_a)

if ("name" in dict_a):
    print ("The Name is {}".format(dict_a["name"]))
else:
    print ("Name doesnot exist")
val=dict_a.get("names")         #if key doesnot present prints None
print (val)


#print the key 
for x  in dict_a:
    print  (x)
    

#print the key-value  pairs
for x,y  in dict_a.items():
    print (x,y)

#insert the key-value pair
dict_a["address"]="bangalore"
dict_a["address"]="gotham"

#delete the key-val pair
del dict_a["address"]

#pop the value and delete from dict
val=dict_a.pop("address", "No address")
print (dict_a)
print (val)
