l=[]
n=int(input("Enter number of elements in a list:"))
if(n>=2):
    for i in range(n):
        x=int(input("Enter a number :"))
        l.append(x)
    l.sort()
else:
    print("Minimun required elements are 2")
    exit()
print("The second smallest number in list is :" , l[1])
