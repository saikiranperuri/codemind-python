a=int(input())
x=0
s=0
while a>0:
    r=a%10
    if r>s:
        s=r
    else:
        s=s
    a=a//10
print(s)
