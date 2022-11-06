t=int(input())
for i in range(t):
    x=int(input())
    e=str(bin(x))
    e=e.replace("0b","")
    print(e)