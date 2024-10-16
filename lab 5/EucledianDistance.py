p1=tuple(map(int,input("ENTER THE FIRST 3D POINT : ").split()))
p2=tuple(map(int,input("ENTER THE SECOND 3D POINT : ").split()))
res=0
for i in range(3):
    res+=(p1[i]-p2[i])**2
res=res**0.5
print(f"THE EUCLEDIAN DISTANCE BETWEEN THE POINTS IS : {res}")
 