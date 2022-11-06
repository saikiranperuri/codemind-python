def getsum(n):
    sum=0
    for digit in str(n):
        sum +=int(digit)
    return sum
 
    
n=int(input())
x=n*n
e=getsum(x)
if(e==n):
    print("Neon Number")
else:
    print("Not Neon Number")