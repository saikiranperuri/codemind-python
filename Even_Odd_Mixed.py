a=int(input())
even=0
odd=0
mixed=0
while a>0:
    r=a%10
    if r%2==0:
        even+=1
    elif r%2!=0:
        odd+=1
    else:
        mixed+=1
    a=a//10
if even>1 and odd==0 and mixed==0:
    print("Even")
elif even==0 and odd>1 and mixed==0:
    print("Odd")
else:
    print("Mixed")
        