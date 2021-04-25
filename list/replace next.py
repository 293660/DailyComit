print("To replace each nth element with its n+1th element in list")
n=int(input("Enter number of elements in a given list : "))
l=[]
for i in range(0,n):
    l.append(str(input("Enter an element : ")))
t=l[0]
for i in range(1, n):
    l[i-1]=l[i]
l[-1]=t
for i in l:
    print(i,end=" ")
