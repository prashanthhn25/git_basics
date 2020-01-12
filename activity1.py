#activity-2
'''
Create a json file named "settings.json" with the following conditions
1) "license" An alphanumeric licence key
2) "username" An user defined username, minimum 6 characters
3) "time" Time in terms of epoch time (Integer Check)
4) "id" An ID ranging between 0 to 100

Operations:
1) Check if all the attributes are available in the file
2) Validate the values
3) if "id" range is between 0 to 50, append "-add" to the
   username if not appended already
4) if Operation had any changes to the settings.json file,
   then write back to the same file, with a operation.log file
   containing username and time of operation
'''


import json
from datetime import datetime
with open("settings.json") as file:
	data=json.loads(file.read())

def log(data):
	with open("logs","a") as file:
		file.write("[{}] : {}".format(datetime.now(),data))

def validateAttributes(entity):
	mandatoryAttributes=["license","username","time","id"]
	for attribute in mandatoryAttributes:
		if(attribute not in entity):
			log("Attribute {} is not Present in the file".format(attribute))
			return False
	return True

def validateValues(entity):
	if(not entity["license"].isalnum()):
		log("Value for Attribute License is invalid")
		return False
	if(len(entity["username"])<6):
		log("Value for Attribute Username is Invalid")
		return False
	if(not isinstance(entity["time"],int)):
		log("Value for Attribute Time is Invalid")
		return False
	if(not 0<int(entity["id"])<100):
		log("Value for Attribute ID is Invalid")
		return False
	return True

flag=False
config=[]
for index,entities in enumerate(data):
	if(validateAttributes(entities)):
		if(validateValues(entities)):
			if(0<int(entities["id"])<50 and "-add" not in entities["username"]):
				entities["username"]+="-add"
				log("The Configuration Changed for {}".format(index))
				config.append(entities)
				flag=True
			else:
				log("The Configuration is Intact for {}".format(index))
				config.append(entities)
		else:
			print ("Attribute Values failed the validation")
			break
	else:
		print ("Attribute Missing for the context")
		break
else:
	if(flag):
		with open("settings.json","w") as file:
			file.write(json.dumps(config,indent=4))


'''
[
    {
        "license": "xyz",
        "username": "prathik-add",
        "time": 52121231,
        "id": 120
    },
    {
        "license": "xyz",
        "username": "prathik-add",
        "time": 52121231,
        "id": 30
    }
]


'''
