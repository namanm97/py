class student:
    name=""
    m2=0
    m1=0
    m3=0
    
    def __init__(self,name,m1,m2,m3): # init constructor
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def calc(self):
        return(self.m1+self.m2+self.m3)
    
    def display(self):
        print "name= ",self.name
        print "m1= ",self.m1
        print "m2= ",self.m2
        print "m3= ",self.m3

n=input("enter name")
m1=int(input("enter marks 1"))
m2=int(input("enter marks 2"))
m3=int(input("enter marks 3"))

s1=student(n,m1,m2,m3)

s1.display()
print "total marks= ",s1.calc()


