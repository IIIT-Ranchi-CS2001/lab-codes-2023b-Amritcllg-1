a,b,c=map(int,input("ENTER THE COEFFICIENTS OF THE QUADRATIC EQUATION : ").split())

d=b**2-(4*a*c)

if d == 0:
    print(f"THE ROOTS OF THE EQUATION ARE : {-1*b/(2*a)}")
    
if d>0:
    print(f"THE ROOTS OF THE EQUATION ARE : {(-1*b+(d**0.5))/(2*a)} and {(-1*b-(d**0.5))/(2*a)}")
    
if d<0:
    real=(-1*b)/(2*a)
    img=(abs(d)**0.5)/(2*a)
    print(f"ROOTS OF THE EQUATION ARE : {real}+i{img} and {real}-i{img}")