a,b=map(int,input().split())
if(a==1 and b==10) or (a==10 and b==1):
    print("Yes")
elif b==a+1 and a==b-1:
    print("Yes")
elif a-1==b and b+1==a:
    print("Yes")
else:
    print("No")

