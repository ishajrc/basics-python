x=input("Enter a string: ")
for i in x:
    if i.isupper():
        print(i.lower(),end="")
    elif i.islower():
        print(i.upper(),end="")