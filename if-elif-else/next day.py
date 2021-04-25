print("To display Next Date")
d=int(input("Enter current date : "))
m=int(input("Enter current month : "))
y=int(input("Enter current year : "))
if((y%4==0 and y%100!=0) or y%400==0):
    if(m==2 and d<=28):
        print(d+1,m,y,sep="-")
elif((d<28 and m==2) or ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d<31) or ((m==4 or m==6 or m==9 or m==11) and d<30)):
    print(d+1,m,y,sep="-")
elif(m==12 and d==31):
    print(1,1,y+1,sep="-")
elif(((m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d==31) or ((m==4 or m==6 or m==9 or m==11) and d==30)):
    print(1,m+1,y,sep="-")