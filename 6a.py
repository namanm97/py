def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0],maximum(l[1:])) #l[1:] #is called slicing

list1=[10,30,40]
print(maximum(list1))
