x=int(input("Enter a number: "))
y=0
for i in range(1,(x//2)+1):
    if x%i == 0 :
        y=y+i
if y==x:
    print("it is perfect")
else:
    print("it is not perfect")
