size=int(input("ENTER THE SIZE OF LIST"))
l=[0]*size #declare list
for i in range(size):
    l[i]=int(input("enter values"))
print(l)
s=[x for x in l if x%2==0] #even
print(s)
l.reverse()
print(l)

