n=int(input("ENTER A NUMBER : "))
s=0
while(n!=0):
    r=n%10
    s+=r
    n=n//10
    
print(f"Sum of digits is {s}")