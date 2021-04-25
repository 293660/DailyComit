print("Program to find the maximum and minimum number of a set")
s=set()
n=int(input("Enter number of elements in a set : "))
for i in range(n):
    v=int(input("Enter a number : "))
    s.add(v)
s=list(s)
s.sort()
print("Minimum Value in a set is : ",s[0])
print("Maximum value of a set is : ",s[-1])

