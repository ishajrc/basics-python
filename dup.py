lst=[1,2,3,2,3,4]
x1=[]
for i in set(lst):
    if lst.count(i)>1:
        x1.append(i)
print(x1,end="")