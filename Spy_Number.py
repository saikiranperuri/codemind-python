a=int(input())
s=0
b=1
while a>0:
    r=a%10
    s +=r
    b *=r
    a=a//10
if s==b:
    print("Spy Number")
else:
    print("Not Spy Number")