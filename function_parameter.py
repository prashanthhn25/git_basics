'''
#passing parameter 
def f1(a):
    print (a)

f1()

#example 1
def f1(a):
    print (a)

f1(1)

#expamle 2
#b is called named parmeter
#a is positional argument 
def f1(a,b=2):
    print ("the value of a is {}".format(a))
    print ("the value of b is {}".format(b))
f1(1)


def f1(a,b=2):
    print ("the value of a is {}".format(a))
    print ("the value of b is {}".format(b))
f1(1,99)


#error
def f1(b=2,a):
    print ("the value of a is {}".format(a))
    print ("the value of b is {}".format(b))
f1(1)


#arguments to the function
#pasisng multiple arguments 
def f2(*args):
    print ("the argumnets are{}".format(args))
#f2(1,2,3,4,5,"Hello World")
f2()        #tuples


#method 1
def f3(a, b=2, *args):
    print ("Value of a is {}".format(a))
    print ("Value of b is {}".format(b))
    print ("argumnets is {}".format(args))

f3(1,2,3,4,5,6)

#method 2
def f3(a,*args,b=2):
    print ("Value of a is {}".format(a))
    print ("Value of b is {}".format(b))
    print ("argumnets is {}".format(args))

f3(1,2,3,4,5,6,b=99)
'''

#pass key value pairs to function
def f4(**kwargs):
    print ("#######kwargs###########")
    print ("Named arguments are {}".format(kwargs))

f4()

#pass key value pairs to function
def f4(**kwargs):
    print ("#######kwargs###########")
    print ("Named arguments are {}".format(kwargs))

f4(name="batman", age=25)


#pass args and kwargs to function
def f3(a,*args,b=2, **kwargs):
    print ("Value of a is {}".format(a))
    print ("Value of b is {}".format(b))
    print ("argumnets is {}".format(args))
    print ("Named argumnets is {}".format(kwargs))
    
f3(1,2,3,4,5,6,b=99, c=99, g=53,d=10)




