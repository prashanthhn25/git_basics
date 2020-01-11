'''
a="Hello World"
print (a[0])
print (a[len(a)-1])
print (a[-1])

print(a[0:5])
print(a[6:11])
print(a[:5])
print(a[6:])
print(a[:])
print(a[::2])       #increment of 2

#a[0]=f         #immutable
'''
a="Hello"
b=4
#c=a+b           #concatinate with string only
c=a+str(b)
print(c)



str=99
temp=str
del str
c=a+str(b)
str=temp
print(c)

 
