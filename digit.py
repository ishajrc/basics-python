lst=["zero","one","two","three","four","five","six","seven","eight","nine"]
x=input()
for i in x:
    if i=="-":
        print("Minus",end=" ")
    else:
        print(lst[int(i)],end=" ")


