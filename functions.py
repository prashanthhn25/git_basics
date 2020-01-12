#functions
'''
def f1():
    print ("Hello World")
f1()
x=f1()
#del f1
x()

#return from the fun
def f1():
    print ("Hello World")

x=f1()
print (x)


def f1():
    print ("Hello World")
    return "Happy Sunday"
x=f1()
print (x)



#exchnage 2 variables
x=5
y=6
print(x,y)
x,y=y,x
print (x,y)


x=5
y=6
print(x,y)
x=y,x
print(x)
print (type(x))

'''
#type
tuple_a=(1)
print (tuple_a)
print (type(tuple_a))


tuple_a=(1,)
print (tuple_a)
print (type(tuple_a))

def f1():
    print ("Hell")
    return "Happy sunday", 1
message, err_code=f1()
print (message)

#enumerate for list
list_a=[1,2,3]
for x in enumerate(list_a):
    print (x)

#map values in list
list_a=[["prathik",100],["Durga", 200], ["Anand", 300]]
for name, age in list_a:
    print (name, age)


