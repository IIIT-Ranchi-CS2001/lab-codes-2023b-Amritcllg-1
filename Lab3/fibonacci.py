n=int(input("ENTER A NUMBER : "))

a=0
b=1

print(f"{a} {b}",end=" ")
n=n-2
while(n>0):
    s=a+b
    print(f"{s}",end=" ")
    a=b 
    b=s 
    n-=1
