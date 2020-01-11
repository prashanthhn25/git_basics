#while loop
a="Hello World"
l=len(a)
i=0
while (i<l):
    print(a[i])
    i=i+1

#else in while
#else is executed only while block is successful
a="Hello World"
l=len(a)
i=0
while (i<l):
    print(a[i])
    i=i+1
else:
    print("Else block is executed")


#while with break    
a="Hello World"
l=len(a)
i=0
while (i<l):
    print(a[i])
    if (i == 4):
        break
    i=i+1
else:
    print("Else block is executed")


#print ("a", "b", sep="")
#print("a"+"b",end="")
print ("Hello",sep=" ")
print("a"+"b",end="")
