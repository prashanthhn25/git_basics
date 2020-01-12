temp=[]
for x in range(10):
    temp.append(x)
print (temp)

temp=[x for x in range(10)]
print (temp)

'''
temp=[]
for x in range(5):
    for y in range(5):
        temp.append([x,y])
print (temp)

temp=[[x,y] for x in range(5) for y in range(5)]
print (temp)


temp=[]
for x in range(5):
    for y in range(5):
        if (x%2==0):
            temp.append([x,y])

print (temp)

temp=[[x,y]for x in range(5) for y in range(5) if (x%2==0)]
print (temp)
'''
#if else in list comprehension
temp=[[x,y] if(x%2==0) else 0 for x in range(5) for y in range(5)]
print (temp)
