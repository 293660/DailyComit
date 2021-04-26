print("To convert  list into a nested dictionary of keys")
l=[1, 2, 3, 4]
d=t={}
for i in l:
    t[i]={}
    t=t[i]
print(d)
