def sdn(a):
    c=1*a
    b=str(a)
    d=0
    for i in range(1,len(b)+1):
        r=a%10
        a=a//10
        if r==0:
            r=c+1
        d=d+c%r
    return d
a=int(input())
b=int(input())
for i in range(a,b+1):
    if sdn(i)==0:
        print(i,end=" ")