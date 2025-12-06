n=int(input())
ans=0
x=n
while x!=0 :
    ans=ans+((x%10)**3)
    x=x//10
if ans==n:
    print("amstrong")
else:
    print("not amstrong")
