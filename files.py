#file handling

'''
# 1) read mode
x=open("sample.txt")        #default read mode
data=x.read()
print (data)
x.close()


x=open("sample.txt", "r")
data=x.read()
print (data)
x.close()

#automatically closes the file
with open("sample.txt") as file:
    print (file.read())

#read the file line by line
with open("sample.txt") as file:
    data=file.readlines()
    print (data)

#using for loop to read the file line by line
with open("sample.txt") as file:
    for x in file:
        print (x,end="")



# 2) write mode
file=open("outcome.json", "w")
file.write("Hello")
file.close()

with open("outcome.json", "w") as file:
    file.write("Hello World")


import json
#writing JSON to a file
configuration={
   "username" : "XYZ",
   "password" : "secret"
   }
with open("config.json", "w") as file:
    file.write(json.dumps(configuration,indent=4))

#reading the JSON form the file
import json
with open("config.json", "r") as file:
    data=json.loads(file.read())
    print (data["username"])
    print (data["password"])
    '''

# 3) append

with open("logs", "a") as file:
    file.write("HEllo World\n")



