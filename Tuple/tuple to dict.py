print("To convert  list of tuples into a dictionary")

def Convert(l, d):
    for a, b in l:
        d.setdefault(a, []).append(b)
    return d

l=[]
n=int(input("How many tuples you want to enter : "))
for i in range(n):
    l1=list(map(str,input("Enter key and value : ").split()))
    l1[1]=int(l1[1])
    l.append(tuple(l1))

d = {}
print(Convert(l, d))
