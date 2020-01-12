'''
#function within functions
def f1(x):
    x()
    print ("F1")
def f2():
    print ("F2")
f1(f2)

#method 2
def f1(data):
    if (isinstance(data, int)):     #check the type using isinstance
        return f2
    else:
        return  f3
    print ("F1")
def f2():
    print ("F2")
def f3():
    print ("F3")

execute=f1("Hello World")
execute()

#other way to pass function as paramater
f1("Hello World")()



#method 3
def f1(data):
    if (isinstance(data, int)):     #check the type using isinstance
        return f2
    else:
        return  f3
    
def f2():
    print ("F2")
    return "This is f2"
def f3():
    print ("F3")
    return "This is f3"

results=f1(1)()
print (results)


#example 1
def backup():
    print ("Taking Backup")
def erase():
    print ("erasing Backup")
def  printer():
    print ("PRinting result")

mapper={
    "1001" : backup,
    "1002" : erase,
    "1003" : printer
    }

command = ["1002", "1010", "1001", "1003"]

for x in command:
    if (x in mapper):
        mapper[x]()
    else:
        print ("commnad is invalid")

'''

#example 2
def backup():
    print ("Taking Backup")
def erase():
    print ("erasing Backup")
def  printer():
    print ("PRinting result")

mapper={
    "1001" : backup,
    "1002" : erase,
    "1003" : printer
    }

allowedMapper={}
allowedMapperxcommand=["1002", "1003"]
for x in allowedMapperxcommand:
    allowedMapper[x]=mapper[x]

command = ["1002", "1010", "1001", "1003"]

for x in command:
    if (x in allowedMapper):
        allowedMapper[x]()
    else:
        print ("commnad is invalid")



