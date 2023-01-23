a=int(input())
b=list(map(int,input().split()))
s=[]
p=[]
for i in b:
    if i%2==0:
        s.append(i)
    elif i%2!=0:
        p.append(i)
print(*s+p)
    
    