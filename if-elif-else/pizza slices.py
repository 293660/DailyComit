print("If number of slices are even then the cost per slice is 120")
print("If number of slices are odd then the cost per slice is 123")
try:
    n=int(input("Enter how many slices:"))
except:
    print("The value entered must be a number")
    exit()
if(n%2==0):
    print(n*120)
else:
    print(n*123)