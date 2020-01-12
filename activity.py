import sys
import json

x=open("settings.JSON", "r")        
data=json.loads(x.read())
x.close()

print (data)

if ("license" in data):
    temp=data["license"]
    isnum=temp.isalnum()
    if (isnum == True):
        print ("The license is alphanumeric key")
    else:
        print ("The license is not a alphanumeric key")
        sys.exit()

    
    if ("username" in data):
        temp=data.get("username")
        length=len(temp)
        if (length >= 6):
            print ("the username is vaild")
        else:
            print ("The username is invalid")
            sys.exit()

    if ("time" in data):
        temp=data.get("time")
        if ((isinstance(temp, int)) == True):
            print ("The time is integer ")
        else:
             print ("The time is not in epoch time")
             sys.exit()

    if ("id" in data):
        temp=data.get("id")
        if (0<temp<100):
            print ("The id is in range")
        else:
             print ("The id is not in the rnage")
             sys.exit()
           
            
    
