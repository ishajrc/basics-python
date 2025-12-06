g=["dood", "cac", "took", "malayalam", "Zooooooyza", "LOOOOOOOOOOOL"]
max=0
for i in g:
    if i.lower()==i.lower()[::-1]:
        l=len(i)
        if l>max:
            max=l
print(max)

