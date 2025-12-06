x= int(input("enter a number"))
y=x*x
len=len(str(x))
if y%(10**len)==x:
    print("it is automorphic")
else:
    print("it is not automorphic")