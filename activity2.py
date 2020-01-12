
'''
Question:
Create a file named "Hosts" without any extension
The Structure of the file is as follows
----------Contents----------
www.facebook.com 192.168.1.1
www.google.com 192.168.1.2
----------------------------
Convert the file to the following 3 JSON Pretty formats 
---------output1.json-------------
[
	{
		"url" : "www.facebook.com",
		"ip"  : "192.168.1.1" 
	},
	{
		"url" : "www.google.com",
		"ip"  : "192.168.1.2" 
	}
]
---------output2.json---------------
[
	["url","ip"],
	["www.facebook.com","192.168.1.1"],
	["www.google.com","192.168.1.2"]
]
--------output3.json----------------
{
	"www.facebook.com" : "192.168.1.1",
	"www.google.com"   : "192.168.1.2"
}
-------------------------------------
SYNTAXS Introduced or which can be used:
---->
file=open("filename")
for x in file:
	print (x)
---->
file=open("filename")
data=file.readlines()
---->
str.split or str.partition
'''


import json
temp=[]
with open("Hosts", "r") as file:
	for x in file:
		data=x.split()
		if(len(data)>=2):
			temp.append([data[0],data[1]])

print (temp)


# Outcome1
outcome1=[]
for url,ip in temp:
	outcome1.append({
		"url" : url,
		"ip" : ip
		})
with open("outcome1.json","w") as file:
	file.write(json.dumps(outcome1,indent=4))

outcome2=list(temp)
outcome2.insert(0,["url","ip"])
with open("outcome2.json","w") as file:
	file.write(json.dumps(outcome2,indent=4))

outcome3={}
for url,ip in temp:
	outcome3[url]=ip
with open("outcome3.json","w") as file:
	file.write(json.dumps(outcome3,indent=4))
'''

 Editable Link  Share Link
Words: 146 | Chars: 1495 | Views: 0
Last Updated: 6 Seconds ago
Privacy  Terms  Contact Us  About Us
'''

