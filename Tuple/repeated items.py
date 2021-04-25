print("To print the repeated items of a given tuple")
n=int(input("Enter number of elements : "))
print("Enter tuple elements with a space in between ")
l=[]
t=tuple(map(str,input().split()))
for i in t:
    if(t.count(i)>1 and i not in l):
        l.append(i)
for i in l:
    print(i)
