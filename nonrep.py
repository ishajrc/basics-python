lst = [4,5,5,3,5,6,7,4,3,6]
for i in set(lst):
    if lst.count(i)<2:
        print(i)