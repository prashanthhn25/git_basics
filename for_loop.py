a="Hello World"
'''
for  i in a:
    print (i)

for  i in a:
    print (i)
else:
    print("Else executed")

#track the index of for loop using enumerate
#works with integers
for x,y in enumerate(a):            #x is index and y is value
    print(x,y)

#reverse the string
for x in a[::-1]:
    print(x)

#range function
for i in range(0, 100):
    print(i)

#same as above value    
for i in range(100):
    print(i)

#print the value in increment of 2
for i in range(0, 100, 2):
    print(i)
 '''   

#using enumerator in for loop
for i,j in enumerate(range(0, 100,5)):
    print(i,j)
