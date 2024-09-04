import math

a,b,c=map(int,input('ENTER 3 SIDES OF THE TRIANGLE : ').split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"PERIMETER OF THE TRAINGLE IS : {a+b+c}")
print(f"AREA OF THE TRAINGLE IS : {area}")


A=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
B=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
C=math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))

print(f"THE ANGLES OF THE TRIANGLE ARE : {A}, {B}, {C}")
