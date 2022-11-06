t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    f=input()
    v=[]
    for i in range(b):
        d=f[:b-i]
        d=d[::-1]
        x=f[b-i:]
        f=d+x
    print(f)