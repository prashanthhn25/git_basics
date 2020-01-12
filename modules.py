'''
#module creation
import sys
print (sys.path)
'''     

#can have import and from twice


import gennames
print (gennames.generate_random_name)           #print the function address
print (gennames.limit_names)           #print the function address

print (gennames.generate_random_name(6))

print (gennames.limit_names("Helo World"))


from gennames import generate_random_name
print (generate_random_name(6))

from gennames import limit_names
print (limit_names("HEllo World"))


#address is same
print (generate_random_name)
print (gennames.generate_random_name)           #print the function address
