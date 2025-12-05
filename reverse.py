x="ELEPHANT"
print(x[5:8])
print(x[0:3])
print(x[3:6])
print(x[7:4:-1])
print(x[::-2])

x=436
r=0
while x!= 0:
    l=x%10
    r=r*10+l
    x=x//10
print(r)